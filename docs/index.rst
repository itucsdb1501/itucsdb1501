Welcome to AthleticInsight's documentation!
===================================

:Team: 1501
================
:Members:

   * Elif Aklan
   * Burak Balta
   * Samet Ayaltı
   * Alper Çakıroğlu
   
====================

PROJECT DESCRIPTION
--------------------
==========
ABSTRACT
=========
  	This report is a result of our Database Management Systems course’s term project. It has all details of project’s process in terms of user guide and develepor guide. The project is a web application named AthleticInsight which is one of the branches of sports. The technologies used are Python (3.4 or later versions) as a programming language, the Flask web framework, and SQL database which should be compatible for access with dbapi2 compatible driver. 
=============
INTRODUCTION
============
	  Database Management System course provides students to learn how to create and manage databases, also create, search, update and delete data in databases systematically. DBMS is such a useful system software in terms of providing centralized point of data which is accessable from several locations by many users. 
	  
    In order to start term project, there should be realized some installation which are git, python and eclipse(Luna edition). As a second step, project setup is realized for GitHub and IBM Bluemix by a team and for Eclipse individually. Last step is database setup is for every member in the group. Besides, In order to set vagrant, virtualbox setup should be realized. Also, to run the project every step requires 'vagrant up' written as a command on terminal. What is more, in order to manage the database localhost::5000 is visited.  What is important is Vagrant has to be set on Oracle Virtualbox to use it. It is so useful and effective to save time for multiple membered projects while working on local. There would be no problem when members of project implementing on server.
    
    .. figure:: vagrant.png
   :scale: 50%
   :alt: map to buried treas
   
	  Also, there is ElephantSQL which can be run on PostgreSQL Servers. This tool is fully integrated with many applications platform like IBM Bluemix which is used for this project. It means that whoever use IBM Bluemix server can reach and see the web application developed by ElephantSQL. Lastly, using GitHub provides the members of project to be able to use the changed and developed code without any concern about the place and time. Building and deploying page after managing database does occur on Jazzhub Page.
	In this project for every member of group there are three object which are related to each other by using foreign keys. Totally twelve objects specify the tables in the database. Besides, every objects have their add, delete, update and search functionality. And mostly they have the relation depending on thir foreing keys. It has also advanced Python and SQL properties, Html, Css, Bootsrap, jQuery improvements are used to for design of tables, as well.
	

Contents:

.. toctree::
   :maxdepth: 1

   user/index
   developer/index
