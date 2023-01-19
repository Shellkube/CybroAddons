from datetime import datetime, timedelta
# from msilib.schema import Error

from requests import request
from odoo import models, fields, api
import logging
import json

_logger = logging.getLogger(__name__)


class ImImportError(models.TransientModel):
    _name = 'display.api.message'

    def get_message(self):
        if self.env.context.get("message", False):
            return self.env.context.get('message')
        return False
    message = fields.Text(string="Message", readonly=True, default=get_message)


class ImLeadWizard(models.TransientModel):
    _name = "im.lead.wizard"
    url = fields.Char("URL")
    st_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    api_key = fields.Char("Api Key")

    def import_indiamart_leads(self):
        delta = timedelta(days=1)
        if not self.st_date or not self.end_date:
            st_date = datetime.now() - delta
            end_date = st_date+delta
            # st_date_f = st_date.strftime("%d-%m-%Y00:00:00")
            # end_date_f = end_date.strftime("%d-%m-%Y%H:%M:%S")
        else:
            st_date = self.st_date
            end_date = self.end_date
            # st_date_f = st_date.strftime("%d-%m-%Y00:00:00")
            # end_date_f = end_date.strftime("%d-%m-%Y24:00:00")
        st_date_f = st_date.strftime("%d-%m-%Y")
        end_date_f = end_date.strftime("%d-%m-%Y")
        api_key = self.env['ir.config_parameter'].get_param('india_mart_api_key', '')
        URL = f"https://mapi.indiamart.com/wservce/crm/crmListing/v2/?glusr_crm_key={api_key}&start_time={st_date_f}&end_time={end_date_f}"
        resp = request("GET", URL)
        # _logger.info(resp.text)
        return self.env['im.leads'].create_leads(resp)
