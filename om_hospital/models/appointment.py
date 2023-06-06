from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"                #  show in database like this (hospital_patient)
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name='patient_id'
    #  _rec_name = 'ref'


    patient_id= fields.Many2one('hospital.patient', string="Patient")
    # patient_id= fields.Many2one(comodel_name='hospital.patient', string="Patient")

    gender = fields.Selection(related ='patient_id.gender')
    # ORR gender = fields.Selection([('male','Male'),('female','Female')],string = "Gender" , related ='patient_id.gender')
    # gender = fields.Selection(related ='patient_id.gender' , readonly=False)  use readonly to change gender
   
    appointment_time = fields.Datetime(String = 'Appointment Time' , default=fields.Datetime.now)
    booking_date = fields.Date(String = 'Booking Date', default=fields.Date.context_today)

    ref = fields.Char(string='Reference', default = 'Odoo Mates')
    prescription = fields.Html(string = 'Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string='Priority')       # 3 stars in view
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string='Status', required=True)


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref


    def action_test(self):
        print("Button Clicked !!!!!!!")

