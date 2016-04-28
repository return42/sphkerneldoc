.. -*- coding: utf-8; mode: rst -*-

==================
RFkill integration
==================

RFkill integration in cfg80211 is almost invisible to drivers, as
cfg80211 automatically registers an rfkill instance for each wireless
device it knows about. Soft kill is also translated into disconnecting
and turning all interfaces off, drivers are expected to turn off the
device when all interfaces are down.

However, devices may have a hard RFkill line, in which case they also
need to interact with the rfkill subsystem, via cfg80211. They can do
this with a few helper functions documented here.


.. toctree::
    :maxdepth: 1

    API-wiphy-rfkill-set-hw-state
    API-wiphy-rfkill-start-polling
    API-wiphy-rfkill-stop-polling




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
