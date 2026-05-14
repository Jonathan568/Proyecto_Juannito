from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Usuarios.models import Alumno

class CicloEscolar(models.Model):
    ESTATUS_CICLO = [
        ('activo', 'Activo (Inscripciones abiertas)'),
        ('en_curso', 'En Curso (Clases)'),
        ('finalizado', 'Finalizado (Histórico)')
    ]
    nombre = models.CharField(max_length=50, unique=True, help_text="Ejemplo: 2026-A")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estatus = models.CharField(max_length=20, choices=ESTATUS_CICLO, default='activo')

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    clave = models.CharField(max_length=20, unique=True, help_text="Ej. MAT-101")
    nombre = models.CharField(max_length=150)
    creditos = models.IntegerField(default=0)
    semestre_ideal = models.IntegerField(default=1, help_text="Semestre en el que se sugiere cursar")
    prerrequisito = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='materias_consecutivas')

    def __str__(self):
        return f"{self.clave} - {self.nombre}"

class Grupo(models.Model):
    nombre = models.CharField(max_length=50) 
    semestre = models.IntegerField(default=1) # Modificado para no pedir default
    idciclo = models.ForeignKey(CicloEscolar, on_delete=models.CASCADE, null=True, blank=True) # Modificado

    def __str__(self):
        if self.idciclo:
            return f"Grupo {self.nombre} ({self.idciclo.nombre})"
        return f"Grupo {self.nombre}"

class AlumnoGrupo(models.Model):
    idalumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    idgrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True, blank=True) # Modificado
    fecha_asignacion = models.DateTimeField(auto_now_add=True, null=True) # Modificado

    class Meta:
        unique_together = ('idalumno', 'idgrupo') 

    def __str__(self):
        return f"{self.idalumno.matricula} en {self.idgrupo.nombre if self.idgrupo else 'Sin grupo'}"

class Horario(models.Model):
    DIAS_SEMANA = [
        ('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sábado')
    ]
    idgrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    idasignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    profesor_asignado = models.CharField(max_length=150, help_text="Nombre del profesor") 
    aula = models.CharField(max_length=50, help_text="Ej. Edificio A - Aula 12")
    dia = models.CharField(max_length=20, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.idasignatura.nombre} - {self.dia} {self.hora_inicio}"

class Inscripcion(models.Model):
    ESTATUS_MATERIA = [
        ('cursando', 'Cursando actualmente'),
        ('aprobada', 'Aprobada'),
        ('reprobada', 'Reprobada'),
        ('baja', 'Dado de Baja')
    ]
    idalumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    idasignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    idciclo = models.ForeignKey(CicloEscolar, on_delete=models.CASCADE)
    
    estatus = models.CharField(max_length=20, choices=ESTATUS_MATERIA, default='cursando')
    calificacion_final = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True, 
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    class Meta:
        unique_together = ('idalumno', 'idasignatura', 'idciclo') 

    def __str__(self):
        return f"{self.idalumno.matricula} - {self.idasignatura.clave}"

class Aviso(models.Model):
    TIPO_AVISO = [
        ('global', 'Todos los alumnos'),
        ('grupal', 'Un grupo en específico'),
        ('individual', 'Un alumno en específico')
    ]
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=TIPO_AVISO, default='global')
    idgrupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True, blank=True)
    idalumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo