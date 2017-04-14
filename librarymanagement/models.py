# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions

class Books(models.Model):
	_name = 'librarymanagement.books'

	title = fields.Char(string="Title", required=True)
	description = fields.Text()
	about = fields.Text()
	author = fields.Char(string="Author", required=True)
	publisher = fields.Char(string="Publisher")
	title = fields.Char(string="Title")
	unit_price = fields.Float()
	quantity = fields.Float()
	price = fields.Float(string="Price", compute='_onchangeprice', store=True)
	edition = fields.Char(string="Book Edition")

	librarian_id = fields.Many2one('res.users',
		ondelete='set null', string="Librarian", index=True)
	issuedbooks_ids = fields.One2many(
		'librarymanagement.issuedbooks', 'book_id', string="Issued Book ID")

	@api.depends('unit_price', 'quantity')
	def _onchangeprice(self):
		# print 'print'
		self.price = self.unit_price * self.quantity



class IssuedBooks(models.Model):
	_name = 'librarymanagement.issuedbooks'

	title = fields.Char(string='Book Title', required=True)
	author = fields.Char(string="Author", required=True)
	studentname = fields.Char(string = 'Student name')
	studentid = fields.Char(string = 'Student ID', required=True)	
	issuedate = fields.Date(string='Issued Date', default=fields.Date.today)
	returndate = fields.Date(string='Return Date')
	bookstatus = fields.Boolean(string='Book Returned',default=False)


	asstlibrarian_id = fields.Many2one('res.partner', string="Assistant Librarian")
	book_id = fields.Many2one('librarymanagement.books',
		ondelete='cascade', string="Book ID", required=True)

	state = fields.Selection([
		('available', "Available"),
		('issued', "Issued"),
		('returned', "Returned"),
	], default='available')

	@api.multi
	def action_available(self):
		self.state = 'available'

	@api.multi
	def action_issued(self):
		self.state = 'issued'

	@api.multi
	def action_returned(self):
		self.state = 'returned'

	@api.multi
	def unlink(self):
		print '**$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$123'
		# rec = super(IssuedBooks, self).unlink(vals)
		# returndate = fields.Date(string='Return Date', default=fields.Date.today)
		print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$xyss'
		return models.Model.unlink(self)

	# @api.model
	# def create(self,values):
 	# rec = super(IssuedBooks, self).unlink(vals)
 	# return rec


@api.constrains('librarian_id', 'asstlibrarian_id')
def _check_librarian_not_in_asstlibrarian(self):
	for r in self:
		if r.librarian_id in r.asstlibrarian_id:
			raise exceptions.ValidationError("An assistant librarian can't be a librarian")



