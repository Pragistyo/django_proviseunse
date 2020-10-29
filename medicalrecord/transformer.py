from .models import MedicalRecords

def transform(values):
    arr = []

    for item in values:
        arr.append(singleTransform(item))

    return arr



def dictTransform(arrDataInserted, doctorInfo):

    return {
            "doctorname" : doctorInfo["doctorName"],
            "currentCountpatientnumber" : doctorInfo["currentCountpatientnumber"],
            "consultDate": arrDataInserted[3],
            "bloodPressure": arrDataInserted[4],
            "bpmNumber": arrDataInserted[5],
            "pupil": arrDataInserted[6],
            "temperature": arrDataInserted[7],
            "polyclinic": arrDataInserted[8]
    }
