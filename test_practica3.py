#!/usr/bin/env python

# WARNING!!!
# this script should be run in a chrooted environment

import os
import pexpect
import random
import re
from subprocess import check_call
import string
import sys
from tempfile import mkstemp
import unittest

class TestPractica3(unittest.TestCase):

    # clean before every test, just in case something goes wrong
    def setUp(self):
        check_call(["./remove_possible_users.sh"])

    def tearDown(self):
        try:
            self.child.terminate(force=True)
        except:
            None

    def test_shebang(self):
        with open('./practica_3.sh') as f:
            first_line = f.readline().rstrip('\r\n')

            pattern=re.compile('#!/usr/bin/env\s+bash')
            # two options: #!/bin/bash or #!/usr/bin/env bash
            self.assertTrue((first_line == '#!/bin/bash') or 
                    (pattern.match(first_line) != None))

    def test_required_commands(self):
        # ToDo fix to skip comments

        required_commands=frozenset(['useradd', 'userdel', 'usermod', 'chpasswd'])

        script_words=set()

        with open('./practica_3.sh') as f:
            for l in f:
                script_words.update([ w.rstrip('\n') for w in l.split()])

        self.assertTrue(script_words.issuperset(required_commands))

    def test_number_arguments(self):
        self.child = pexpect.spawn('sudo /bin/bash ./practica_3.sh -a correct_user_list.txt extra_arg')
        try:
            self.child.expect_exact('Numero incorrecto de parametros\r\n')
        except:
            self.assertTrue(False)
        self.assertTrue(True)

    def test_sudo(self):
        self.child = pexpect.spawn('/bin/bash ./practica_3.sh -a correct_user_list.txt')
        try:
            self.child.expect_exact('Este script necesita privilegios de administracion')
        except:
            self.assertTrue(False)
        self.assertTrue(True)
    
    def test_invalid_argument(self):
        self.child = pexpect.spawn('sudo -- /bin/bash ./practica_3.sh -I correct_user_list.txt')
        try:
            self.child.expect_exact('Opcion invalida')
        except:
            self.assertTrue(False)
        self.assertTrue(True)

    def test_correct_user_list(self):
        self.child = pexpect.spawn('sudo -- /bin/bash ./practica_3.sh -a ./correct_user_list.txt')

        with open('./correct_user_list.txt', 'r') as f:
            for line in f:
                user, pwd, name = [ w.rstrip(' \n').lstrip(' ') for w in line.split(',') ]
                try:
                    expected_string="{} ha sido creado".format(name)
                    self.child.expect_exact(expected_string)
                except:
                    self.assertTrue(False)
        self.assertTrue(True)

    def test_root_user(self):
        self.child = pexpect.spawn('sudo -- /bin/bash ./practica_3.sh -a incorrect_user_list_existing_root.txt')

        try:
            self.child.expect_exact('El usuario root ya existe')
        except:
            self.assertTrue(False)

        self.assertTrue(True)


    def test_existing_user(self):

        # create user
        users=set()
        with open('/etc/passwd', 'r') as f:
            for line in f:
                users.add(line.split(':')[0])

        random_user_name=''.join(random.choice(string.ascii_letters+string.digits) for _ in range(8))
        while random_user_name in users:
            random_user_name=''.join(random.choice(string.ascii_letters+string.digits) for _ in range(8))

        tmp_handle, tmp_name = mkstemp()

        check_call(["sudo", "useradd", "{}".format(random_user_name)])

        os.write(tmp_handle, '{}, {}, {}\n'.format(random_user_name, 'pwd', 'name'))
        os.close(tmp_handle)

        null_file=open(os.devnull, 'w')
        
        self.child = pexpect.spawn('sudo', ['--', '/bin/bash', './practica_3.sh', '-a', tmp_name])

        try:
            expected_string='El usuario {} ya existe'.format(random_user_name)
            self.child.expect_exact(expected_string)
        except:
            # ensure the newly created user is deleted
            check_call(["sudo", "userdel", "-r", "-f", "{}".format(random_user_name)], 
                    stdout=null_file, stderr=null_file)
            self.assertTrue(False)
            os.unlink(tmp_name)
            null_file.close()

        self.assertTrue(True)
        check_call(["sudo", "userdel", "-r", "-f", "{}".format(random_user_name)],
                    stdout=null_file, stderr=null_file)
        os.unlink(tmp_name)
        null_file.close()

if __name__ == "__main__":
    unittest.main()