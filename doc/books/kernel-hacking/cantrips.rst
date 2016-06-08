.. -*- coding: utf-8; mode: rst -*-

.. _cantrips:

***************
Kernel Cantrips
***************

Some favorites from browsing the source. Feel free to add to this list.

``arch/x86/include/asm/delay.h:``


.. code-block:: c

    #define ndelay(n) (__builtin_constant_p(n) ? 
            ((n) > 20000 ? __bad_ndelay() : __const_udelay((n) * 5ul)) : 
            __ndelay(n))

``include/linux/fs.h``:


.. code-block:: c

    /*
     * Kernel pointers have redundant information, so we can use a
     * scheme where we can return either an error code or a dentry
     * pointer with the same return value.
     *
     * This should be a per-architecture thing, to allow different
     * error and pointer decisions.
     */
     #define ERR_PTR(err)    ((void *)((long)(err)))
     #define PTR_ERR(ptr)    ((long)(ptr))
     #define IS_ERR(ptr)     ((unsigned long)(ptr) > (unsigned long)(-1000))

``arch/x86/include/asm/uaccess_32.h:``


.. code-block:: c

    #define copy_to_user(to,from,n)                         
            (__builtin_constant_p(n) ?                      
             __constant_copy_to_user((to),(from),(n)) :     
             __generic_copy_to_user((to),(from),(n)))

``arch/sparc/kernel/head.S:``


.. code-block:: c

    /*
     * Sun people can't spell worth damn. "compatability" indeed.
     * At least we *know* we can't spell, and use a spell-checker.
     */

    /* Uh, actually Linus it is I who cannot spell. Too much murky
     * Sparc assembly will do this to ya.
     */
    C_LABEL(cputypvar):
            .asciz "compatibility"

    /* Tested on SS-5, SS-10. Probably someone at Sun applied a spell-checker. */
            .align 4
    C_LABEL(cputypvar_sun4m):
            .asciz "compatible"

``arch/sparc/lib/checksum.S:``


.. code-block:: c

            /* Sun, you just can't beat me, you just can't.  Stop trying,
             * give up.  I'm serious, I am going to kick the living shit
             * out of you, game over, lights out.
             */




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
