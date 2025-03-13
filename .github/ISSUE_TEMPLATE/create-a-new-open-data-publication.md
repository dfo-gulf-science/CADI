---
name: New - Open Data Publication
about: boilerplate for creating a new open data publication
title: 'OPEN DATA: [insert name here] (NEW)'
labels: ''
assignees: davjfish, RobichaudA

---

Data Custodian:
- [ ] Complete metadata record in DMApps (bilingual)
- [ ] Provide image, data dictionary, dataset, and shapfile (for Web Map Services) [either via storage section or confirm info is in GitHub]
- [ ] Certify the record
- [ ] Flag for publication

Data Steward (CADI):

DMApps
- [ ] Internal CADI review of metadata record
  - [ ] The metadata record should be fully bilingual
  - [ ] Image, data dictionary, dataset, and shapefile (zip) are available
  - [ ] Dataset should be a one to one relationship (one column to one row with intersecting data)
  - [ ] Dataset table headers are bilingual [the data in the table does not need to be bilingual]
  - [ ] Data Dictionary is bilingual (make sure the headers match the dataset table)
  - [ ] No merged cells are permitted
  - [ ] Lat and long coordinates have their own header and formatted to decimal degrees
    - [ ]  + latitude northern hemisphere, - longitude western hemisphere (ISO 6709 compliance)
  - [ ]  Date and time fields should conform to : yyyy-mm-ddThh:mm:ss [shift relative to UTC]
    - [ ]  If no time data provided, provide data in the following format: yyyy-mm-dd (ISO 8601 are expected)
  - [ ] If a shapefile is not provided by the data custodian and you have the GIS skills to create a shapefile using the dataset provided, you may proceed. Otherwise, IMTS can create the WMS.
- [ ] Validate the record
- [ ] Export XML from DMApps

EDH 

- [ ] Import XML in EDH as a new record
- [ ] Add resources (CSVs, etc.) and provide metadata for each resource (use DFO.GLFCSA-CASGLF.MPO@dfo-mpo.gc.ca as the contact email)
- [ ] Complete level 1 review and attach as a resource (internal use only)
- [ ] **
- [ ] Submit request for WMS via EDH
- [ ] Once REST service has been created, check to make sure that data is valid and approve the service in the Service Request Dashboard
- [ ] Add the English and French WMS as resources
- [ ] Validate your record - Do one last QA/QC of your EDH record to make sure that all links work and that "add to map" buttons appear for the WMS resources
- [ ] Redo your level 1 review and update the recource
- [ ] **
- [ ] Complete the Release Criteria Checklist (RCC) and attach the final copy (with signatures) as a recource (internal use only
- [ ] **
- [ ] Send email to Shane Servant to advise that the record is ready for external publication

** Approve your working copy
-   [ ] If you have the EDH reviewer role you can validate your record yourself, if you do not have this role - send your record for review

DMApps
- [ ] Update the metadata record in DMApps
  - [ ] Add public URL for image
  - [ ] Add URL for EDH record
  - [ ] Add public URLs for Data Resources (dataset, data dictionary, WMS EN/FR etc.)
  - [ ] Update publication date
  - [ ] Unflag for publication if not already done
