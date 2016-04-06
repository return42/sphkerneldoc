
.. _deadlock-recipes:

====================
Recipes for Deadlock
====================

You cannot call any routines which may sleep, unless:

-  You are in user context.

-  You do not own any spinlocks.

-  You have interrupts enabled (actually, Andi Kleen says that the scheduling code will enable them for you, but that's probably not what you wanted).

Note that some functions may sleep implicitly: common ones are the user space access functions (⋆_user) and memory allocation functions without ``GFP_ATOMIC``.

You should always compile your kernel ``CONFIG_DEBUG_ATOMIC_SLEEP`` on, and it will warn you if you break these rules. If you *do* break the rules, you will eventually lock up your
box.

Really.
