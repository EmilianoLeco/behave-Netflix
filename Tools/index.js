var reporter = require('cucumber-html-reporter');

var today = new Date();
var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
var time = today.getHours() + "-" + today.getMinutes() + "-" + today.getSeconds();
var dateTime = date+'_'+time;
var Sdate = date.toString();
var Stime = time.toString();
var dateTime = Sdate + '_' + Stime;

var options = {
        theme: 'bootstrap',
        name: 'Tests Cases',
        //jsonDir: 'Reports'
        brandTitle: 'Acceptance test report',
        jsonFile: 'Reports/cucumber.json',
        output: 'Reports/cucumber_report-' + dateTime + ".html",
        screenshotsDirectory: 'screenshots/',
        storeScreenshots: true,
        reportSuiteAsScenarios: true,
        scenarioTimestamp: true,
        launchReport: false,
        metadata: {
            "App Version":"1.1",
            "Test Environment": "QA 4",
            "Browser": "Chrome  76.0.3809.87",
            "Platform": "Debian",
            "Parallel": "Scenarios",
            "Executed": "Remote"
        }
    };
 
    reporter.generate(options);