job('First-Maven-Project-via-DSL') {
    description("First Maven job generated by the DSL on ${new Date()}, the project is a small Maven project hosted on github")
    scm {
        git("git@github.com:irdanish11/devops.git", 'main')
        // credentials("danish (SSH Key for GitHub)")
        credentialsId("jenkins-github")
    }
    triggers {
        scm('* * * * *')
    }
    steps {
        maven('clean package', 'maven-samples/single-module/pom.xml')
    }
    publishers {
        //archive the war file generated
        archiveArtifacts '**/*.jar'
    }
}