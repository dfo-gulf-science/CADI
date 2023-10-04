---
name: Create a New Open Data Publication
about: boilerplate for creating a new open data publication
title: 'OPEN DATA: [insert name here] (NEW)'
labels: 'open data'
assignees: RobichaudA
projects: CADI Board

---
- [ ] Identify data steward
- [ ] Data steward to complete metadata record in DMApps
- [ ] Data steward to provide image, data dictionary, dataset, and shapfile (for Web Map Services) [either via storage section or confirm info is in GitHub]
- [ ] Data steward to certify metadata record
- [ ] Internal CADI review of metadata record
  - [ ] The metadata record should be fully bilingual
  - [ ] Image, data dictionary, dataset, and shapefile (zip) are available
  - [ ] Dataset should be a one to one relationship (one column to one row with intersecting data)
  - [ ] Dataset table headers are bilingual [the data in the table does not need to be bilingual]
  - [ ] Data Dictionary is bilingual
  - [ ] No merged cells are permitted
  - [ ] Lat and long coordinates have their own header and formatted to decimal degrees
    - [ ]  + latitude northern hemisphere, - longitude western hemisphere (ISO 6709 compliance)
  - [ ]  Date and time fields should conform to : yyyy-mm-ddThh:mm:ss [shift relative to UTC]
    - [ ]  If no time data provided, provide data in the following format: yyyy-mm-dd (ISO 8601 are expected)
  - [ ] If a shapefile is not provided by the data steward and you have the GIS skills to create a shapefile using the dataset provided, you may proceed. Otherwise, IMTS can create the WMS on behalf of the data steward.
- [ ] CADI to validate record
- [ ] Export XML from DMApps and import in EDH as a new record
- [ ] CADI to perform review and validation of uploaded XML in EDH
- [ ] Submit request for WMS via EDH
- [ ] Once WMS has been created, update the EDH record with the URL and complete a final review of the EDH record by completing a level 1 review
-   [ ] If you have the EDH reviewer role you can validate your record yourself, if you do not have this role - send your record for review
- [ ] Once the EDH record has been validated (either by yourself or someone from EDH) you can now send it for internal and external publication
  - [ ]  Send email to Shane Servant with your level 1 review attached and advise that the record is ready for external publication
- [ ] Update the metadata record in DMApps
  - [ ] Add public URL for image
  - [ ] Add URL for EDH record
  - [ ] Add public URLs for Data Resources (dataset and data dictionary)
  - [ ] Add public URLs for WMS (EN and FR)
  - [ ] Update publication date
