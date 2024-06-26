#
# Copyright (C) 2020  FreeIPA Contributors see COPYING for license
#
"""RHEL container paths
"""
import os

from ipaplatform.rhel.paths import RHELPathNamespace


def data(path):
    return os.path.join("/data", path[1:])


class RHELContainerPathNamespace(RHELPathNamespace):
    KRB5_CONF = data(RHELPathNamespace.KRB5_CONF)
    KRB5_KEYTAB = data(RHELPathNamespace.KRB5_KEYTAB)
    NAMED_KEYTAB = data(RHELPathNamespace.NAMED_KEYTAB)
    NAMED_CUSTOM_CONF = data(RHELPathNamespace.NAMED_CUSTOM_CONF)
    NAMED_CUSTOM_OPTIONS_CONF = data(
        RHELPathNamespace.NAMED_CUSTOM_OPTIONS_CONF
    )
    NAMED_LOGGING_OPTIONS_CONF = data(
        RHELPathNamespace.NAMED_LOGGING_OPTIONS_CONF
    )
    NSSWITCH_CONF = data(RHELPathNamespace.NSSWITCH_CONF)
    PKI_CONFIGURATION = data(RHELPathNamespace.PKI_CONFIGURATION)
    SAMBA_DIR = data(RHELPathNamespace.SAMBA_DIR)
    HTTPD_IPA_WSGI_MODULES_CONF = None
    HTTPD_PASSWD_FILE_FMT = data(RHELPathNamespace.HTTPD_PASSWD_FILE_FMT)

    # In some contexts, filesystem mounts may be owned by unmapped users
    # (e.g. "emptyDir" mounts in Kubernetes / OpenShift when using user
    # namespaces).  This causes systemd-tmpfiles(8) to fail, as a
    # consequence of systemd's path processing routines which reject
    # this scenario.  Therefore we provide a way to substitute
    # systemd-tmpfiles with a "clone" program.
    #
    SYSTEMD_TMPFILES = os.environ.get(
        'IPA_TMPFILES_PROG', RHELPathNamespace.SYSTEMD_TMPFILES)


paths = RHELContainerPathNamespace()
