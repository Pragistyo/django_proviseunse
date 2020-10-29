queryInsert = '''
        WITH i AS (
            INSERT INTO medicalrecord
            (medicalrecord_id, inpatient_id, doctor_id, consultdate, bloodpressure, bpmnumber ,pupil, temperature, polyclinic)
            VALUES 
            (DEFAULT, %s,%s,%s, %s,
            %s, %s, %s,%s)
            RETURNING *
        )
        UPDATE doctor AS a
            SET countpatientnumber = countpatientnumber + 1
            FROM i
            WHERE i.doctor_id = a.doctor_id
        RETURNING i, countpatientnumber, firstname, middlename, lastname
        '''
queryRemove =  '''
        WITH u AS (
            UPDATE doctor 
            SET countpatientnumber = countpatientnumber - 1
            WHERE 
                doctor.doctor_id = (SELECT doctor_id FROM medicalrecord WHERE medicalrecord_id = %s) 
            RETURNING *
        )
        DELETE from medicalrecord WHERE medicalrecord_id = %s
        RETURNING *
        '''

queryMedicalRecordDateRange='''
        WITH u AS(
            SELECT *
                FROM medicalrecord 
                LEFT OUTER JOIN inpatient
                ON medicalrecord.inpatient_id = inpatient.inpatient_id
            WHERE 
                consultdate 
            BETWEEN %s AND %s
        )
        SELECT polyclinic,
            COUNT(*) OVER(),
            SUM(CASE WHEN bloodtype = 'O' then 1 else 0 end )OVER() AS bloodtype_O,
            SUM(CASE WHEN bloodtype = 'A' then 1 else 0 end )OVER() AS bloodtype_A,
            SUM(CASE WHEN bloodtype = 'B' then 1 else 0 end )OVER() AS bloodtype_B,
            SUM(CASE WHEN bloodtype = 'AB' then 1 else 0 end )OVER() AS bloodtype_AB
        FROM u
    '''

queryMedicalRecordDateRangePolyclinic ='''
             WITH u AS(
                SELECT * 
                    FROM medicalrecord 
                    LEFT OUTER JOIN inpatient
                    ON medicalrecord.inpatient_id = inpatient.inpatient_id
                WHERE 
                    polyclinic = %s
                AND 
                    consultdate BETWEEN %s AND %s
            )
            SELECT polyclinic,
                COUNT(*) OVER(),
                SUM(CASE WHEN bloodtype = 'O' then 1 else 0 end )OVER() AS bloodtype_O,
                SUM(CASE WHEN bloodtype = 'A' then 1 else 0 end )OVER() AS bloodtype_A,
                SUM(CASE WHEN bloodtype = 'B' then 1 else 0 end )OVER() AS bloodtype_B,
                SUM(CASE WHEN bloodtype = 'AB' then 1 else 0 end )OVER() AS bloodtype_AB
            FROM u
        '''