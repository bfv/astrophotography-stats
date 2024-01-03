
import astropy.io.fits as fits
from datetime import datetime, timedelta

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
        self.focallength = hdul[0].header['FOCALLEN']

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
  FL        : {self.focallength}
  camera    : {self.camera}
  filter    : {self.filter}
  obs date  : {self.observation_date}
  date      : {self.date}
  exposure  : {self.exposure}s
  RA/Dec    : {self.ra}, {self.dec} (deg)
  software  : {self.software}
        '''
        return str
    
    def __get_date(self, date_str):
        date = (datetime.fromisoformat(date_str) - timedelta(hours=12)).date()
        return date

    def __get_software(self, hdul) -> str:
        software = ""
        if self.__has_header(hdul, "CREATOR"):     # ASIAIR
            software = hdul[0].header["CREATOR"]
        elif self.__has_header(hdul, "SWCREATE"):  # N.I.N.A.
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
            
if __name__ == "__main__":
    ic434 = FitsFile(r"D:\onedrive\_2023\ic434\lights\Light_IC434_180.0s_Bin1_eXtr_20230208-193136_0001.fit", "IC434")
    print(ic434)
    sn2023ixf = FitsFile(r"D:\onedrive\_2023\m101_sn2023ixf\m101_1\lights\Light_M101_120.0s_Bin1_Pro_20230519-033042_0098.fit", "M101")
    print(sn2023ixf)
    m51 = FitsFile(r"D:\onedrive\_2023\m51e\lights\Light_M51_180.0s_Bin1_Pro_20230228-235224_0017.fit", "M51")
    print(m51)
    sh2_155 = FitsFile(r"D:\onedrive\_2023\sh2-155\lights\Sh2 155_2023-12-17_18-01-57_HaOiii_-10.00_120.00s_0002.fits", "SH2-155")
    print(sh2_155)
    ngc6946 = FitsFile(r"D:\onedrive\_2023\ngc6946e\lights\LIGHT_NGC 6946_2023-09-10_23-47-59_UVIR_-9.60_60.00s_0011.fits", "NGC6946")
    print(ngc6946)
