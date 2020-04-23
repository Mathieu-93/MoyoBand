class Patient:

    def __init__(self, first, last, ID, TEMP, BMP):
        self.first = first
        self.last = last
        self.ID = ID
        self.BMP = BMP
        self.TEMP = TEMP

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def PatientInformation(self):
        return 'Patient with {}: BMP:{} TEMP: {}'.format(self.ID, self.BMP, self.TEMP)

    def __repr__(self):
        return "Patient('{}','{}','{}')".format(self.first, self.last, self.ID)
