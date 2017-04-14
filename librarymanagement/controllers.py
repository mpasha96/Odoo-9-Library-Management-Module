# -*- coding: utf-8 -*-
from openerp import http

# class Librarymanagement(http.Controller):
#     @http.route('/librarymanagement/librarymanagement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/librarymanagement/librarymanagement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('librarymanagement.listing', {
#             'root': '/librarymanagement/librarymanagement',
#             'objects': http.request.env['librarymanagement.librarymanagement'].search([]),
#         })

#     @http.route('/librarymanagement/librarymanagement/objects/<model("librarymanagement.librarymanagement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('librarymanagement.object', {
#             'object': obj
#         })