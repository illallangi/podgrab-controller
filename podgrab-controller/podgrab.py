import kopf

CRD_GROUP = "controllers.illallangi.enterprises"
CRD_VERSION = "v1"
CRD_SINGULAR = "podgrab"


@kopf.index(
    group=CRD_GROUP,
    version=CRD_VERSION,
    singular=CRD_SINGULAR,
)
async def podgrab_idx(
    namespace,
    body,
    **_,
):
    return {
        namespace: {k: body[k] for k in body},
    }


@kopf.on.probe(
    id=podgrab_idx.__name__,
)
async def podgrab_probe(
    podgrab_idx: kopf.Index,
    **_,
):
    return {
        namespace: [o for o in podgrab_idx[namespace]]
        for namespace in podgrab_idx
    }
