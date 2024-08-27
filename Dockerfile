FROM ros:humble

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TZ=Europe/Moscow

ENV ROS_DISTRO humble


# ................................................................................................
# Install necessary dependencies .................................................................

RUN apt-get update && apt-get install -y --fix-missing \
  python3 \
  python3-pip \
  python3-colcon-common-extensions \
  && rm -rf /var/lib/apt/lists/*

# ................................................................................................
# copy pkgs ......................................................................................

COPY ./template_pkg /ros2ws/src/template_pkg

# ................................................................................................
# build pkgs .....................................................................................

RUN /bin/bash -c '. /opt/ros/$ROS_DISTRO/setup.bash; cd /ros2ws/ && colcon build --symlink-install'

# ................................................................................................
# setup ros environment ..........................................................................

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
RUN echo "source /ros2ws/install/setup.bash" >> ~/.bashrc

# ................................................................................................
# setup entrypoint ...............................................................................

COPY ./ros_entrypoint.sh /
RUN chmod 755 ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["bash"]
