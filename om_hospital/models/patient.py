
from datetime import date
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"                #  show in database like this (hospital_patient)
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    _description = "Hospital Patient"
    # _rec_name ='name'    By default no need to deine b/c we have made name field


    name = fields.Char(string="Name" , tracking = True)
    date_of_birth= fields.Date(string="Date of Birth")

    ref = fields.Char(string='Reference', default = 'Odoo Mates')
    
    # age = fields.Integer(string="Age", tracking = True)
    age = fields.Integer(string="Age",compute='_compute_age',tracking = True)

    gender = fields.Selection([('male','Male'),('female','Female')],string = "Gender" , tracking = True, default='female')
    active = fields.Boolean(String="Active", default=True)
    # appointment_id = fields.many2One('hospital.appointment', string="Patient") -- ERRoR




    @api.depends('date_of_birth')       ### decorator

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1
       
        