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
        else:
            st_date = self.st_date
            end_date = self.end_date
        st_date_f = st_date.strftime("%d-%m-%Y")
        end_date_f = end_date.strftime("%d-%m-%Y")
        link = f"https://mapi.indiamart.com/wservce/enquiry/listing/GLUSR_MOBILE/9818114474/GLUSR_MOBILE_KEY/MTU5NzY2NjYyNy43ODUjMTU2MDAwMg==/Start_Time/{st_date_f}/End_Time/{end_date_f}/"
        resp = request("GET", link)
        # _logger.info(resp.text)
        return self.env['im.leads'].create_leads(resp)
