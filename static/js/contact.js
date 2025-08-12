document.addEventListener("DOMContentLoaded", function() {
    const emailElement = document.getElementById("virtual-mail");
    const githubElement = document.getElementById("git-hub");
    const linkedinElement = document.getElementById("linked-in");

    // github maker
    const domainGit = "github";
    const userGit = "BrialexMaga";
    const topDomain = "com";

    githubElement.href = `https://${domainGit}.${topDomain}/${userGit}`;
    githubElement.textContent = `${domainGit}.${topDomain}/${userGit}`;

    // linkedin maker
    const domainLinked = "linkedin";
    const firstSection = "in";
    const userLinked = "brian-magana";

    linkedinElement.href = `https://${domainLinked}.${topDomain}/${firstSection}/${userLinked}`;
    linkedinElement.textContent = `${domainLinked}.${topDomain}/${firstSection}/${userLinked}`;

    // e-mail maker
    /*
    const user = "brian.alexis.p1999";
    const domain = "gmail";

    emailElement.textContent = `${user}@${domain}.${topDomain}`;
    */
});