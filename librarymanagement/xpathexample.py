# -*- coding: utf-8 -*-
from openerp import fields, models, api

class xpathexample(models.Model):
    _inherit = 'librarymanagement.books'

    # Add a new filed to the librarymanagment.books model,
    asstlibrarian = fields.Boolean("Asst librarian", default=False)

    # book_ids = fields.Many2many('librarymanagement.issuedbooks',
    #     string="Issued Books", readonly=True)

    standardprice = fields.Text(string="standard price")