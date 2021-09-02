import unittest


class FirstTest(unittest.TestCase):
    def test_a(self):
        self.assertEqual('a', 'b', 'a and b are not equal')

    def test_db(self):
        import  repository.sqlite_helper as sql
        sql.init_connection()

        sql.commit("insert into users(url) values (?)", ['http://localhost:8080'])

        new_var = sql.execute('select * from users;')
        print(new_var)
    
    def test_get_all_hosts(self):
        import repository.sqlite_helper as sql
        sql.init_connection()
        import repository.hosts as h
        result = h.get_all_hosts()
        print('got result')

        print(list(result))


if __name__ == '__main__':
    unittest.main()
