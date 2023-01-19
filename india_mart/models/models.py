# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
# from msilib.schema import Error

from requests import request
from odoo import models, fields, api
import logging
import json

_logger = logging.getLogger(__name__)


# class git_saas/testing/india_mart(models.Model):
#     _name = 'git_saas/testing/india_mart.git_saas/testing/india_mart'
#     _description = 'git_saas/testing/india_mart.git_saas/testing/india_mart'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class ImLeads(models.TransientModel):
    _name = "im.leads"
    query_id = fields.Char(string="Unique query id")
    sender_name = fields.Char("Name")
    product_details = fields.Text(string="Product Details")
    state = fields.Char(string="State")
    city = fields.Char(string="City")
    contact = fields.Char(string="Contact person")
    email = fields.Char(string="Email")
    email2 = fields.Char(string="Email2")
    mobile = fields.Char(string="Contact Number")
    mobile2 = fields.Char(string="Contact Number2")
    message = fields.Text(string="Message")
    subject = fields.Text(string="Subject")
    date1 = fields.Char(string="Enquiry Date")
    datetime1 = fields.Char("Enquiry Time")
    glusr_usr_companyname = fields.Char("Company Name")
    street = fields.Text(string="Street Address")
    product_name = fields.Char(string="Product Name")
    country_iso = fields.Char("Country ISO")
    query_type = fields.Char("Query Type")

    """"“UNIQUE_QUERY_ID”: “2012487827”,
   “QUERY_TYPE”: “W”,
            “QUERY_TIME”: “2021-12-08 12:47:25”,
            “SENDER_NAME”: “Arun”,
            “SENDER_MOBILE”: “+91-999XXXXXXX”,
            “SENDER_EMAIL”: “arunxyz@gmail.com”,
            “SENDER_COMPANY”: “Arun Industries”,
            “SENDER_ADDRESS”: “Arun Industries, Meerut, Uttar Pradesh, 250001”,
            “SENDER_CITY”: “Meerut”,
            “SENDER_STATE”: “Uttar Pradesh”,
            “SENDER_COUNTRY_ISO”: “IN”,
            “SENDER_MOBILE_ALT”: null,
            “SENDER_EMAIL_ALT”: “arunxyz1@gmail.com”,
            “QUERY_PRODUCT_NAME”: “Dye Sublimation Ink”,
            “QUERY_MESSAGE”: “I want to buy Dye Sublimation Ink.”,
            “CALL_DURATION”: null,
            “RECEIVER_MOBILE”: null
"""
    @api.model
    def fetch_leads(self):
        delta = timedelta(days=1)
        st_date = datetime.now() - delta
        end_date = st_date+delta
        st_date_f = st_date.strftime("%d-%m-%Y")
        end_date_f = end_date.strftime("%d-%m-%Y")
        # import wdb; wdb.set_trace()
        api_key = self.env['ir.config_parameter'].get_param('india_mart_api_key', '')
        URL = f"https://mapi.indiamart.com/wservce/crm/crmListing/v2/?glusr_crm_key={api_key}&start_time={st_date_f}&end_time={end_date_f}"
        resp = request("GET", URL)
        try:
            data = json.loads(resp.text)
            for rec in data['RESPONSE']:
                # _logger.info(rec)
                _logger.info(rec['UNIQUE_QUERY_ID'])
                if rec['SENDER_MOBILE']:
                    rec['SENDER_MOBILE'] = rec['SENDER_MOBILE'].replace("-", "")
                res = super(ImLeads, self).create(
                    {'query_id': rec['UNIQUE_QUERY_ID'],
                     'sender_name': rec['SENDER_NAME'],
                     'datetime1': rec['QUERY_TIME'],
                     'date1': rec['QUERY_TIME'],
                     'email': rec['SENDER_EMAIL'],
                     'state': rec['SENDER_STATE'],
                     'city': rec['SENDER_CITY'],
                     'mobile': rec['SENDER_MOBILE'],
                     'subject': rec['SUBJECT'],
                     'product_name': rec['QUERY_PRODUCT_NAME'],
                     'glusr_usr_companyname': rec['SENDER_COMPANY'],
                     'street': rec['SENDER_ADDRESS'],
                     'email2': rec['SENDER_EMAIL_ALT'],
                     'mobile2': rec['SENDER_MOBILE_ALT'],
                     'message': rec['QUERY_MESSAGE'],
                     'query_type': rec['QUERY_TYPE']})
            return res
        except Exception as e:
            _logger.info(f"could not import due to {e}")

    @api.model
    def create_leads(self, resp):
        try:
            data = json.loads(resp.text)
            # import wdb; wdb.set_trace()
            for rec in data['RESPONSE']:
                # _logger.info(rec)
                # _logger.info(rec['QUERY_ID'])
                if rec['SENDER_MOBILE']:
                    rec['SENDER_MOBILE'] = rec['SENDER_MOBILE'].replace("-", "")
                if rec['QUERY_TYPE'] == 'W':
                    rec['QUERY_TYPE'] = 'Direct'
                elif rec['QUERY_TYPE'] == 'B':
                    rec['QUERY_TYPE'] = 'Consumed BuyLead'
                elif rec['QUERY_TYPE'] == 'P':
                    rec['QUERY_TYPE'] = 'Call'
                else:
                    pass
                res = super(ImLeads, self).create(
                    {'query_id': rec['UNIQUE_QUERY_ID'],
                     'sender_name': rec['SENDER_NAME'],
                     'datetime1': rec['QUERY_TIME'],
                     'date1': rec['QUERY_TIME'],
                     'email': rec['SENDER_EMAIL'],
                     'state': rec['SENDER_STATE'],
                     'city': rec['SENDER_CITY'],
                     'mobile': rec['SENDER_MOBILE'],
                     'subject': rec['SUBJECT'],
                     'product_name': rec['QUERY_PRODUCT_NAME'],
                     'glusr_usr_companyname': rec['SENDER_COMPANY'],
                     'street': rec['SENDER_ADDRESS'],
                     'email2': rec['SENDER_EMAIL_ALT'],
                     'mobile2': rec['SENDER_MOBILE_ALT'],
                     'message': rec['QUERY_MESSAGE'],
                     'query_type': rec['QUERY_TYPE']})
            return res
        except Exception as e:
            _logger.info(f"could not import due to {e}")
            context = {'message': resp.text}
            return {
                "type": "ir.actions.act_window",
                "name": "Api error encountered",
                "res_model": "display.api.message",
                "domain": [],
                "view_mode": "form",
                "view_type": "form",
                "target": "new",
                "context": context,
            }
