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

    """"RN": "2",
        "QUERY_ID": "463179622",
        "QTYPE": "B",
        "SENDERNAME": "Mahinder Kumar",
        "SENDEREMAIL": "dr.mkk1008@gmail.com",
        "SUBJECT": "Requirement for Semi Automated Biochemistry Analyzer",
        "DATE_RE": "16 Apr 2022",
        "DATE_R": "16-Apr-22",
        "DATE_TIME_RE": "16-Apr-2022 09:33:16 AM",
        "GLUSR_USR_COMPANYNAME": "Dr Education Center",
        "READ_STATUS": null,
        "SENDER_GLUSR_USR_ID": null,
        "MOB": "+91-9672746032",
        "COUNTRY_FLAG": "",
        "QUERY_MODID": "DIRECT",
        "LOG_TIME": "20220416093316",
        "QUERY_MODREFID": null,
        "DIR_QUERY_MODREF_TYPE": null,
        "ORG_SENDER_GLUSR_ID": null,
        "ENQ_MESSAGE": "I want to buy Semi Automated Biochemistry Analyzer.\n\nKindly send me price and other details.<br>Automation : Semi Automatic<br>Usage\/Application : for lab use<br>Probable Requirement Type : Business Use",
        "ENQ_ADDRESS": "Station Road,nawalgarh , Jhunjhunun, Rajasthan",
        "ENQ_CALL_DURATION": null,
        "ENQ_RECEIVER_MOB": null,
        "ENQ_CITY": "Jhunjhunun",
        "ENQ_STATE": "Rajasthan",
        "PRODUCT_NAME": "Semi Automated Biochemistry Analyzer",
        "COUNTRY_ISO": "IN",
        "EMAIL_ALT": "mnikhil108@gmail.com",
        "MOBILE_ALT": "+91-9887967469",
        "PHONE": null,
        "PHONE_ALT": null,
        "IM_MEMBER_SINCE": null,
        "TOTAL_COUNT": "19"
"""
    @api.model
    def fetch_leads(self):
        delta = timedelta(days=1)
        st_date = datetime.now() - delta
        end_date = st_date+delta
        st_date_f = st_date.strftime("%d-%m-%Y")
        end_date_f = end_date.strftime("%d-%m-%Y")
        api_key = self.env['ir.config_parameter'].get_param('india_mart_api_key', '')
        URL = f"https://mapi.indiamart.com/wservce/crm/crmListing/v2/?glusr_crm_key={api_key}&start_time={st_date_f}&end_time={end_date_f}"
        resp = request("GET", URL)
        try:
            data = json.loads(resp.text)
            for rec in data:
                # _logger.info(rec)
                _logger.info(rec['QUERY_ID'])
                if rec['MOB']:
                    rec['MOB'] = rec['MOB'].replace("-", "")
                res = super(ImLeads, self).create(
                    {'query_id': rec['QUERY_ID'],
                     'datetime1': rec['DATE_TIME_RE'],
                     'date1': rec['DATE_RE'],
                     'sender_name': rec['SENDERNAME'],
                     'email': rec['SENDEREMAIL'],
                     'state': rec['ENQ_STATE'],
                     'city': rec['ENQ_CITY'],
                     'mobile': rec['MOB'],
                     'subject': rec['SUBJECT'],
                     'product_name': rec['PRODUCT_NAME'],
                     'glusr_usr_companyname': rec['GLUSR_USR_COMPANYNAME'],
                     'street': rec['ENQ_ADDRESS'],
                     'email2': rec['EMAIL_ALT'],
                     'mobile2': rec['MOBILE_ALT'],
                     'message': rec['ENQ_MESSAGE']})
            return res
        except Exception as e:
            _logger.info(f"could not import due to {e}")

    @api.model
    def create_leads(self, resp):
        try:
            data = json.loads(resp.text)
            for rec in data:
                # _logger.info(rec)
                # _logger.info(rec['QUERY_ID'])
                if rec['MOB']:
                    rec['MOB'] = rec['MOB'].replace("-", "")
                res = super(ImLeads, self).create(
                    {'query_id': rec['QUERY_ID'],
                     'sender_name': rec['SENDERNAME'],
                     'datetime1': rec['DATE_TIME_RE'],
                     'date1': rec['DATE_RE'],
                     'email': rec['SENDEREMAIL'],
                     'state': rec['ENQ_STATE'],
                     'city': rec['ENQ_CITY'],
                     'mobile': rec['MOB'],
                     'subject': rec['SUBJECT'],
                     'product_name': rec['PRODUCT_NAME'],
                     'glusr_usr_companyname': rec['GLUSR_USR_COMPANYNAME'],
                     'street': rec['ENQ_ADDRESS'],
                     'email2': rec['EMAIL_ALT'],
                     'mobile2': rec['MOBILE_ALT'],
                     'message': rec['ENQ_MESSAGE']})
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
