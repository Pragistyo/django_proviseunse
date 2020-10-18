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
        "lastname": values.middlename,
        "mobilenumber": values.mobilenumber,
        "gender": values.gender,
        "address1": values.address1,
        "address2": values.address2,
        "state": values.state,
        "city": values.city,
        "zipcode": values.zipcode,
        "birthplace": values.birthday,
        "birthday": values.birthday,
        "nik": values.nik,
        "specialization": values.specialization,
        "certificate": values.certificate,
        "datecertification": values.datecertification,
        "countpatientnumber": values.certificate

       
    }