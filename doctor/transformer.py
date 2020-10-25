from .models import Doctors

def transform(values):
    arr = []

    for item in values:
        arr.append(singleTransform(item))

    return arr


def singleTransform(values):
    return {
        "id": values.doctor_id,
        "firstname": values.firstname,
        "middlename": values.middlename,
        "lastname": values.lastname,
        "mobilenumber": values.mobilenumber,
        "gender": values.gender,
        "address1": values.address1,
        "address2": values.address2,
        "state": values.state,
        "city": values.city,
        "zipcode": values.zipcode,
        "birthplace": values.birthplace,
        "birthday": values.birthday,
        "nik": values.nik,
        "specialization": values.specialization,
        "certificate": values.certificate,
        "datecertification": values.datecertification,
        "countpatientnumber": values.countpatientnumber 
    }
def arraySingleTransform(values):
    return {
        "id": values[0],
        "firstname": values[1],
        "middlename": values[2],
        "lastname": values[3],
        "mobilenumber": values[4],
        "gender": values[5],
        "address1": values[6],
        "address2": values[7],
        "state": values[8],
        "city": values[9],
        "zipcode": values[10],
        "birthplace": values[11],
        "birthday": values[12].strftime('%Y-%m-%d'),
        "nik": values[13],
        "specialization": values[14],
        "certificate": values[15],
        "datecertification": values[16].strftime('%Y-%m-%d'),
        "countpatientnumber": values[17] 
    }

def transformJsonToObject (values) :
    doctor = Doctors()
    # "id": values.['doctor_id'],
    doctor.firstname= values['firstname']
    doctor.middlename= values['middlename']
    doctor.lastname= values['lastname']
    doctor.mobilenumber= values['mobilenumber']
    doctor.gender= values['gender']
    doctor.address1= values['address1']
    doctor.address2= values['address2']
    doctor.state= values['state']
    doctor.city= values['city']
    doctor.zipcode= values['zipcode']
    doctor.birthplace= values['birthplace']
    doctor.birthday= values['birthday']
    doctor.nik= values['nik']
    doctor.specialization= values['specialization']
    doctor.certificate= values['certificate']
    doctor.datecertification= values['datecertification']
    doctor.countpatientnumber= values['countpatientnumber']

    return doctor

