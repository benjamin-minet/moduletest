# -*- coding: utf-8 -*-
import time
from odoo import api, fields, models, _

class BankManagement(models.Model):
    _name = "bank.manage"
    _description = "Bank Management"
    _order = "date"
    
    name = fields.Char(string = "Libelle transaction")
    account = fields.Float(string = "Numéro compte")
    amount = fields.Float(string = "Montant")
    date = fields.Date(string = "Date")
    ope_typ = fields.Selection([('depot', 'Depot'), ('retr', 'Retrait')], string = "Type de transaction")
    
