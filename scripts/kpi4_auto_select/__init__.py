"""KPI4 trial-only execution-config selector (T3/T4)."""

from .selector import (
    POLICY_VERSION,
    BundleProfile,
    SelectionDecision,
    WorkBundleSpec,
    select_execution_config,
)

__all__ = [
    "POLICY_VERSION",
    "BundleProfile",
    "SelectionDecision",
    "WorkBundleSpec",
    "select_execution_config",
]
