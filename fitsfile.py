
import astropy.io.fits as fits
from datetime import *

class FitsFile:

    def __init__(self, filename, target):
        self.file = filename
        self.__parse_file()
        self.target = target

    def __parse_file(self):
        try:
            hdul = fits.open(self.file)
            self.is_fits = True
        except:
            self.is_fits = False
            return

        # essential info
        self.camera = hdul[0].header['INSTRUME']
        self.exposure = int(hdul[0].header['EXPOSURE'])
        self.filter = hdul[0].header['FILTER']
        self.observation_date = hdul[0].header['DATE-OBS'] + "Z"
        self.telescope = hdul[0].header['TELESCOP']
            
        try:
            self.ra = hdul[0].header['RA']
            self.dec = hdul[0].header['DEC']
        except:
            pass

        # derived
        self.date = self.__get_date(self.observation_date)
        self.software = self.__get_software(hdul)

    def __str__(self) -> str:
        str = f'''
fits: {self.file}
  telescope : {self.telescope}
  camera    : {self.camera}
  filter    : {self.filter}
  obs date  : { self.observation_date}
  date      : { self.date}
  exposure  : {self.exposure}s
  RA/Dec    : {self.ra}, {self.dec}
  software  : {self.software}
        '''
        return str
    
    def __get_date(self, date_str):
        #date_format = '%Y-%m-%dT%H:%M:%SZ'
        datetime_obj = datetime.fromisoformat(date_str) - timedelta(hours=12)
        return datetime_obj.date()

    def __get_software(self, hdul) -> str:
        software = ""
        if self.__has_header(hdul, "CREATOR"):
            software = hdul[0].header["CREATOR"]
        elif self.__has_header(hdul, "SWCREATE"):
            software = hdul[0].header["SWCREATE"]
        else:
            software = "<unknown>"
        return software

    def __has_header(self, hdul, key) -> bool:
        result = True
        try:
            tmp = hdul[0].header[key]
        except:
            result = False
        return result
            