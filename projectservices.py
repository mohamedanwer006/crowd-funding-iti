from project import *
from fileservices import *


projects_path="projects"

class PServices:

    @staticmethod
    def add_project(project:Project):
        data = project.to_json()
        add_data(projects_path, data+"\n")
        

    @staticmethod
    def del_project(title,owner):
        deleted=False
        listofproj=PServices.get_projects()
        for i in range(len(listofproj)):
            if listofproj[i].title == title and  listofproj[i].owner == owner :
               del listofproj [i]
               deleted=True
               break
            else :
                return deleted
        if deleted:
            clear_file(projects_path)
            for p in listofproj:
                PServices.add_project(p)
        return deleted

    @staticmethod
    def update_project(project:Project):
        p = project
        return p

    @staticmethod
    def get_projects():
        projects = read_data(projects_path).splitlines()
        projlist=list()
        for p in projects:
           proj=Project.from_json(p)
           projlist.append(proj)
        return projlist










