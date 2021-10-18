from odoo import models, fields

class Modu(models.Model):
    _name = "wb.modu"

    name = fields.Char("Nombre")
