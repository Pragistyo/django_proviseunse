from .models import MedicalRecords

def transform(values):
    arr = []

    for item in values:
        arr.append(singleTransform(item))

    return arr



def dictTransformCreate(arrDataInserted, doctorInfo):

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

def dictTransformMedicalRecord(value):
    return{
        "medicalrecord_id":value[0],
        "inpatient_id": value[1],
        "doctor_id": value[2],
        "consultdate": value[3].strftime('%Y-%m-%d'),
        "bloodpressure": value[4],
        "bpmnumber": value[5],
        "pupil": value[6],
        "temperature": str(value[7]),
        "polyclinic": value[8],
    }

def dictTransformGetByDate(value):
        return{
            "polyclinic": value[0],
            "consult_total": str(value[1]) + " times",
            "ab_bloodtype" : str(value[5])+ " times",
            "a_bloodtype" : str(value[4])+ " times",
            "b_bloodtype" : str(value[3])+ " times",
            "o_bloodtype" : str(value[2])+ " times"
        }
