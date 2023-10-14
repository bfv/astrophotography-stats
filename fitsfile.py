
import astropy.io.fits as fits
from datetime import *

class FitsFile:

    def __init__(self, filename):
        self.file = filename
        self.__parse_file()
        #self.to_string()

    def __parse_file(self):
        try:
            hdul = fits.open(self.file)
            self.is_fits = True
        except:
            self.is_fits = False
            return

        self.camera = hdul[0].header['INSTRUME']
        self.dec = self.ra = hdul[0].header['DEC']
        self.exposure = hdul[0].header['EXPOSURE']
        self.filter = hdul[0].header['FILTER']
        self.observation_date = hdul[0].header['DATE-OBS'] + "Z"
        self.ra = hdul[0].header['RA']
        self.telescope = hdul[0].header['TELESCOP']

        # derived
        self.date = self.__get_date(self.observation_date)
        self.software = self.__get_software(hdul)

    def to_string(self):
        print("fits:", self.file)
        print(f"  telescope : {self.telescope}")
        print(f"  camera    : {self.camera}")
        print(f"  filter    : {self.filter}")    
        print(f"  obs date  : { self.observation_date}")
        print(f"  date      : { self.date}")
        print(f"  exposure  : {self.exposure}s")
        print(f"  RA/Dec    : {self.ra}, {self.dec}")
        print(f"  software  : {self.software}")


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
            