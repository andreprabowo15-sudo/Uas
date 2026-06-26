class Mahasiswa:
    def __init__(self, nim, nama, email, jurusan, semester, ipk):
        self.__nim = nim
        self.__nama = nama
        self.__email = email
        self.__jurusan = jurusan
        self.__semester = semester
        self.__ipk = ipk

    def to_dict(self):
        return {
            "NIM": self.__nim,
            "Nama": self.__nama,
            "Email": self.__email,
            "Jurusan": self.__jurusan,
            "Semester": self.__semester,
            "IPK": self.__ipk
        }

    def status(self):
        return "Mahasiswa Aktif"


class MahasiswaBeasiswa(Mahasiswa):
    def status(self):
        return "Mahasiswa Beasiswa"
