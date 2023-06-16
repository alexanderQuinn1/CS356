import database_connection as db


def insert(passage_id, date_time, cell_count, ph, osmolality, sterility, passed):
    query = """ 
        INSERT INTO passage_qa(passage_d, date_time, cell_count, ph, osmolality, sterility, passed)
        VALUES(%s, %s, %s, %s, %s, %s, %s);
        """

    db.commit(query, (passage_id, date_time, cell_count, ph, osmolality, sterility, passed))
