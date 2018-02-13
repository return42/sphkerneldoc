.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/cifs/connect.c

.. _`cifs_setup_ipc`:

cifs_setup_ipc
==============

.. c:function:: int cifs_setup_ipc(struct cifs_ses *ses, struct smb_vol *volume_info)

    helper to setup the IPC tcon for the session

    :param struct cifs_ses \*ses:
        *undescribed*

    :param struct smb_vol \*volume_info:
        *undescribed*

.. _`cifs_setup_ipc.description`:

Description
-----------

A new IPC connection is made and stored in the session
tcon_ipc. The IPC tcon has the same lifetime as the session.

.. _`cifs_free_ipc`:

cifs_free_ipc
=============

.. c:function:: int cifs_free_ipc(struct cifs_ses *ses)

    helper to release the session IPC tcon

    :param struct cifs_ses \*ses:
        *undescribed*

.. _`cifs_free_ipc.description`:

Description
-----------

Needs to be called everytime a session is destroyed

.. _`cifs_get_smb_ses`:

cifs_get_smb_ses
================

.. c:function:: struct cifs_ses *cifs_get_smb_ses(struct TCP_Server_Info *server, struct smb_vol *volume_info)

    get a session matching \ ``volume_info``\  data from \ ``server``\ 

    :param struct TCP_Server_Info \*server:
        *undescribed*

    :param struct smb_vol \*volume_info:
        *undescribed*

.. _`cifs_get_smb_ses.description`:

Description
-----------

This function assumes it is being called from \ :c:func:`cifs_mount`\  where we
already got a server reference (server refcount +1). See
\ :c:func:`cifs_get_tcon`\  for refcount explanations.

.. _`cifs_get_tcon`:

cifs_get_tcon
=============

.. c:function:: struct cifs_tcon *cifs_get_tcon(struct cifs_ses *ses, struct smb_vol *volume_info)

    get a tcon matching \ ``volume_info``\  data from \ ``ses``\ 

    :param struct cifs_ses \*ses:
        *undescribed*

    :param struct smb_vol \*volume_info:
        *undescribed*

.. _`cifs_get_tcon.description`:

Description
-----------

- tcon refcount is the number of mount points using the tcon.
- ses refcount is the number of tcon using the session.

1. This function assumes it is being called from \ :c:func:`cifs_mount`\  where
we already got a session reference (ses refcount +1).

2. Since we're in the context of adding a mount point, the end

.. _`cifs_get_tcon.result-should-be-either`:

result should be either
-----------------------


a) a new tcon already allocated with refcount=1 (1 mount point) and
its session refcount incremented (1 new tcon). This +1 was
already done in (1).

b) an existing tcon with refcount+1 (add a mount point to it) and
identical ses refcount (no new tcon). Because of (1) we need to
decrement the ses refcount.

.. This file was automatic generated / don't edit.

