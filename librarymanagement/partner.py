# -*- coding: utf-8 -*-
from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    asstlibrarian = fields.Boolean("Asst librarian", default=False)

    book_ids = fields.Many2many('librarymanagement.issuedbooks',
        string="Issued Books", readonly=True)