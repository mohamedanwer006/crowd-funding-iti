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
        deleted = False
        project_index=0

        listofproj= PServices.get_projects()

        for i in range(len(listofproj)):
            # check if the user is owned project with the title
 
            if listofproj[i].title == title and  listofproj[i].owner == owner :
               project_index=i
               deleted=True
        
        if deleted:
            del listofproj[project_index]
            clear_file(projects_path)
            for p in listofproj:
                PServices.add_project(p)
        return deleted

    @staticmethod
    def update_project(updated_project:Project,old_project:Project,owner):
        deleted = PServices.del_project(old_project.title,owner)
        if deleted :
            PServices.add_project(updated_project)
            return True
        else :
            return False

    @staticmethod
    def get_projects():
        projects = read_data(projects_path).splitlines()
        projlist=list()
        for p in projects:
           proj=Project.from_json(p)
           projlist.append(proj)
        return projlist    
    
    @staticmethod
    def get_project(title,owner):
        projects = read_data(projects_path).splitlines()
        for p in projects:
            proj=Project.from_json(p)
            if proj.title == title and proj.owner == owner:
                return proj
        return None
            
        










