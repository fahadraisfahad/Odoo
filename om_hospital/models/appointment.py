from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"                #  show in database like this (hospital_patient)
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    _description = "Hospital Appointment"


    patient_id= fields.Many2one('hospital.patient', string="Patient")
    # patient_id= fields.Many2one(comodel_name='hospital.patient', string="Patient")

    gender = fields.Selection(related ='patient_id.gender')
    # ORR gender = fields.Selection([('male','Male'),('female','Female')],string = "Gender" , related ='patient_id.gender')
    # gender = fields.Selection(related ='patient_id.gender' , readonly=False)  use readonly to change gender
   
    appointment_time = fields.Datetime(String = 'Appointment Time' , default=fields.Datetime.now)
    booking_date = fields.Date(String = 'Booking Date', default=fields.Date.context_today)

