
.. _submitting:

================================
Putting Your Stuff in the Kernel
================================

In order to get your stuff into shape for official inclusion, or even to make a neat patch, there's administrative work to be done:

-  Figure out whose pond you've been pissing in. Look at the top of the source files, inside the ``MAINTAINERS`` file, and last of all in the ``CREDITS`` file. You should
   coordinate with this person to make sure you're not duplicating effort, or trying something that's already been rejected.

   Make sure you put your name and EMail address at the top of any files you create or mangle significantly. This is the first place people will look when they find a bug, or when
   *they* want to make a change.

-  Usually you want a configuration option for your kernel hack. Edit ``Kconfig`` in the appropriate directory. The Config language is simple to use by cut and paste, and there's
   complete documentation in ``Documentation/kbuild/kconfig-language.txt``.

   In your description of the option, make sure you address both the expert user and the user who knows nothing about your feature. Mention incompatibilities and issues here.
   *Definitely* end your description with “if in doubt, say N” (or, occasionally, `Y'); this is for people who have no idea what you are talking about.

-  Edit the ``Makefile``: the CONFIG variables are exported here so you can usually just add a "obj-$(CONFIG_xxx) += xxx.o" line. The syntax is documented in
   ``Documentation/kbuild/makefiles.txt``.

-  Put yourself in ``CREDITS`` if you've done something noteworthy, usually beyond a single file (your name should be at the top of the source files anyway). ``MAINTAINERS`` means
   you want to be consulted when changes are made to a subsystem, and hear about bugs; it implies a more-than-passing commitment to some part of the code.

-  Finally, don't forget to read ``Documentation/SubmittingPatches`` and possibly ``Documentation/SubmittingDrivers``.
