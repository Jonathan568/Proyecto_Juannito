from django.db import models

class Concepto(models.Model):
    idconcepto = models.AutoField(db_column='idConcepto', primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True  # ¡Salto de control activo!
        db_table = 'Concepto'
        verbose_name = "Concepto de Pago"
        verbose_name_plural = "Conceptos Arancelarios"

    # Representación limpia que muestra el nombre y el precio base en los selectores
    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class Pago(models.Model):
    idpago = models.AutoField(db_column='idPago', primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estatus = models.CharField(max_length=20, default='pendiente')  # Ampliado a 20 caracteres y con default
    folio = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True  # ¡Salto de control activo!
        db_table = 'Pago'
        verbose_name = "Transacción / Recibo"
        verbose_name_plural = "Historial de Pagos Recibidos"

    # Muestra un formato impecable con folio, cantidad y estado de la transacción
    def __str__(self):
        folio_str = self.folio if self.folio else f"ID-{self.idpago}"
        estatus_str = self.estatus.upper() if self.estatus else "PENDIENTE"
        return f"Folio: {folio_str} — ${self.monto} [{estatus_str}]"


class CargoAlumno(models.Model):
    idcargo = models.AutoField(db_column='idCargo', primary_key=True)
    
    # Llaves foráneas aseguradas con reglas de integridad relacional
    idalumno = models.ForeignKey('Usuarios.Alumno', models.CASCADE, db_column='idAlumno')
    idconcepto = models.ForeignKey('Concepto', models.PROTECT, db_column='idConcepto')
    idpago = models.ForeignKey('Pago', models.SET_NULL, db_column='idPago', blank=True, null=True)
    
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    estatus = models.CharField(max_length=20, default='pendiente')  # Ampliado a 20 caracteres y con default

    class Meta:
        managed = True  # ¡Salto de control activo!
        db_table = 'Cargo_Alumno'
        verbose_name = "Cargo a Estudiante"
        verbose_name_plural = "Estados de Cuenta (Cargos)"

    # Desglosa visualmente a qué alumno pertenece, el concepto y la cantidad
    def __str__(self):
        try:
            concepto_str = self.idconcepto.nombre
            matricula_str = self.idalumno.matricula
            return f"Ref: {self.idcargo:05d} — {concepto_str} (${self.monto}) — Alumno: {matricula_str}"
        except AttributeError:
            return f"Cargo #{self.idcargo} — ${self.monto}"