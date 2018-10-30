from django.test import TestCase

import datetime
from django.utils import timezone
from .models import Todo
from django.urls import reverse
from django.test import Client


# Create your tests here.

class Testing(TestCase):
    def test(self):
        # get test
        c = Client(enforce_csrf_checks=False)
        response = c.get("/todolist/")
        self.assertEqual(response.status_code,200)

        # addition test (failure)
        response = c.post("/todolist/",{"add":True,})
        self.assertContains(response,"*To add a schedule, please enter all the entries correctly",html=True)
        
        # addition test (success)
        response = c.post("/todolist/",{"add":True,"title":"test","content":"test","priority":5,"due":timezone.now()})
        self.assertContains(response,"<tr class=\"entry\">",html=False)
        self.assertContains(response,"<input type=\"submit\" value=\"Modify\" name=\"modify1\">",html=False)

        # modify_mode test
        response = c.post("/todolist/",{"modify1":True})
        self.assertContains(response,"<tr class=\"modify\">",html=False)
        self.assertNotContains(response,"<tfoot>",html=False)
        self.assertNotContains(response,"<div class=\"query\">",html=False)

        # modify test
        response = c.post("/todolist/",{"modifyas1":True,"priority2":0})
        self.assertContains(response,"<th>0</th>",html=False)

        # done test
        self.assertContains(response,"<span class=\"X\">X</span> ",html=False)
        response = c.post("/todolist/",{"todo1":True,"done":True})
        self.assertContains(response,"<span class=\"O\">O</span>",html=False)

        # remove test
        response = c.post("/todolist/",{"todo1":True,"remove":True})
        self.assertNotContains(response,"<tr class=\"entry\">",html=False)



