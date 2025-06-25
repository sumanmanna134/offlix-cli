FROM jenkins/jenkins:lts

USER root

# Install required dependencies
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    gnupg \
    apt-transport-https \
    ca-certificates \
    software-properties-common \
    sudo

# Install Java (OpenJDK 17)
RUN apt-get install -y openjdk-17-jdk
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Install .NET 6 SDK via Microsoft install script (works for Debian)
RUN wget https://dot.net/v1/dotnet-install.sh -O dotnet-install.sh && \
    chmod +x dotnet-install.sh && \
    ./dotnet-install.sh --version 6.0.414 --install-dir /usr/share/dotnet && \
    ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet && \
    rm dotnet-install.sh

# Install Maven 3.9.6
ENV MAVEN_VERSION=3.9.6
ENV MAVEN_HOME=/opt/maven/apache-maven-${MAVEN_VERSION}
ENV PATH="${MAVEN_HOME}/bin:${PATH}"

RUN mkdir -p /opt/maven && \
    wget https://downloads.apache.org/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz -O /tmp/maven.tar.gz && \
    tar -xzf /tmp/maven.tar.gz -C /opt/maven && \
    rm /tmp/maven.tar.gz

# Verify installation
RUN java -version && \
    dotnet --version && \
    mvn -version

USER jenkins
