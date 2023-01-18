# -*- coding: utf-8 -*-
# from odoo import http


# class GitSaas/testing/indiaMart(http.Controller):
#     @http.route('/git_saas/testing/india_mart/git_saas/testing/india_mart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/git_saas/testing/india_mart/git_saas/testing/india_mart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('git_saas/testing/india_mart.listing', {
#             'root': '/git_saas/testing/india_mart/git_saas/testing/india_mart',
#             'objects': http.request.env['git_saas/testing/india_mart.git_saas/testing/india_mart'].search([]),
#         })

#     @http.route('/git_saas/testing/india_mart/git_saas/testing/india_mart/objects/<model("git_saas/testing/india_mart.git_saas/testing/india_mart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('git_saas/testing/india_mart.object', {
#             'object': obj
#         })
