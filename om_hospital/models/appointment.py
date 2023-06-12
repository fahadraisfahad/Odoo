from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"                #  show in database like this (hospital_patient)
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    _description = "Hospital Appointment"      # same as class name
    _rec_name='patient_id'
    #  _rec_name = 'ref'


    patient_id= fields.Many2one('hospital.patient', string="Patient")
    # patient_id= fields.Many2one(comodel_name='hospital.patient', string="Patient")

    gender = fields.Selection(related ='patient_id.gender')
    # ORR gender = fields.Selection([('male','Male'),('female','Female')],string = "Gender" , related ='patient_id.gender')
    # gender = fields.Selection(related ='patient_id.gender' , readonly=False)  use readonly to change gender
   
    appointment_time = fields.Datetime(String = 'Appointment Time' , default=fields.Datetime.now)
    booking_date = fields.Date(String = 'Booking Date', default=fields.Date.context_today)

    # ref = fields.Char(string='Reference', default = 'Odoo Mates')
    ref = fields.Char(string='Reference', help="Reference from patient record")
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
    
    doctor_id = fields.Many2one('res.users',string='Doctor',tracking=True)   # id in Many2One
    pharmacy_lines_ids =fields.One2many('appointment.pharmacy.lines','appointment_id',string='Pharmacy Lines')  # id(s) in One2many


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref


    def action_test(self):
        print("Button Clicked !!!!!!!")   # show in notepad
        return{
            'effect' : {
                'fadeout':'slow',     # Rainbow disappear automaticaly
                'message':'Click Successful',
                'type':'rainbow_man',
            } 
        }
    
    def action_in_consultation(self):
        for rec in self:                     # rec means record
            rec.state = 'in_consultation'   


    def action_done(self):
        for rec in self:                     
            rec.state = 'done'
    


    def action_cancel(self):
        for rec in self:                 
            rec.state = 'cancel'


    def action_draft(self):
        for rec in self:                 
            rec.state = 'draft'


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"                #  show in database like this (hospital_patient)
    _description = "Appointment Pharmacy Lines"   # same as class name

    product_id=fields.Many2one('product.product')
    # price_unit=fields.Float(string="Price")
    price_unit=fields.Float(string="Price")
    qty=fields.Integer(String="Quantity")
    appointment_id=fields.Many2one('hospital.appointment',string='Appointment')

