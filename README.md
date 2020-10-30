# django_proviseunse
##This is my first project using python django

This project is about API implementation of mini hospital application.  
There are three subjects on this project: Doctor, Patients, medical records.  
This project build by python-Django + PostgrestSQL

## ROUTES

### Main URL
localhost:PORT/provisions/api/v1

### Accepted Header
'application/json'

#### Doctor Routes EndPoint

| Route                             |  HTTP  | Description |
| --------------------------------- | ------ | --------------|
| `/doctors`      | GET    | Get all doctors data
| `/doctors`      | POST   | Create one doctor data
| `/:id/doctor`  | GET    | Get one doctor data
| `/:id/doctor`  | PUT    | Update one doctor data
| `/:id/doctor`  | DELETE | Delete one doctor data


#### Inpatient Routes

| Route                                |  HTTP  | Description |
| ------------------------------------ | ------ | --------------|
| `/inpatient`      | GET    | Get all Inpatients data
| `/inpatient`      | POST   | Create one Inpatient data
| `/:id/inpatient`  | GET    | Get one Inpatient data
| `/:id/inpatient`  | PUT    | Update one Inpatient data
| `/:id/inpatient`  | DELETE | Delete one Inpatient data


#### Medical Records Routes

Medical Records Routes have several feature:
- When Create Medical Records, increase "countpatientnumber" field in doctor table, for ralated doctor
- When Delete Medical Records, decrease "countpatientnumber field in doctor table, for related doctor
- getByDatePolyclinic: input the range dateFrom and dateTo, to get data count all patient which consult at those that. Furthermore, count patient based on their blood type

| Route                                                    |  HTTP  | Description |
| -------------------------------------------------------- | ------ | --------------|
| `/medicalRecord`                       | GET    | Get all medicalRecord data
| `/medicalRecord`                       | POST   | Create one medicalRecord data
| `/medicalRecord/customQuery/getBydatePolyclinic`      | POST   | Return consult sum by date interval and/or selected polyclinic
| `/:id/medicalRecord`                   | GET    | Get one medicalRecord data
| `/:id/medicalRecord`                   | PUT    | Update one medicalRecord data
| `/:id/medicalRecord`                   | DELETE | Delete one medicalRecord data
