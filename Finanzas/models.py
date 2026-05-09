from django.db import models

class Concepto(models.Model):
    idconcepto = models.AutoField(db_column='idConcepto', primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'Concepto'

    def __str__(self):
        return self.nombre

class Pago(models.Model):
    idpago = models.AutoField(db_column='idPago', primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estatus = models.CharField(max_length=10, blank=True, null=True)
    folio = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pago'

    def __str__(self):
        return f"Folio: {self.folio} - {self.estatus}"

class CargoAlumno(models.Model):
    idcargo = models.AutoField(db_column='idCargo', primary_key=True)
    idalumno = models.ForeignKey('Usuarios.Alumno', models.DO_NOTHING, db_column='idAlumno')
    idconcepto = models.ForeignKey('Concepto', models.DO_NOTHING, db_column='idConcepto')
    idpago = models.ForeignKey('Pago', models.DO_NOTHING, db_column='idPago', blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    estatus = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cargo_Alumno'

    def __str__(self):
        return f"Cargo {self.idcargo} - ${self.monto}"