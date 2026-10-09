# Project 10: Pineda Salon Co., Biometric Privacy Assessment

**A privacy impact assessment of an AI skin-diagnostic kiosk that a marketing team bought, installed in nine salons, and never sent through contract or privacy review.**

> ⚠️ **Fictional organization. Created for portfolio demonstration purposes.** Pineda Salon Co. and Oduya Imaging, Inc. do not exist. No client, biometric, or vendor record described here is real. Regulatory citations are for demonstration and are not legal advice. See [DISCLAIMER](../DISCLAIMER.md).

---

## The scenario

Pineda runs seven salons in Brevard and Orange counties, Florida, and two in the Houston area. Three of the nine are booth-rental locations, where stylists are independent businesses leasing chairs.

In February 2026 the retail marketing lead bought SkinRead kiosks from Oduya Imaging on a standard order form. A client stands at the kiosk, has her face photographed, can opt into a 3D face-geometry capture, and gets a skin and scalp report that recommends services and retail products. The vendor keeps the images and trains its models on them. No data processing addendum was signed, and the vendor intake checklist had no question about client data, so nobody in operations or legal saw the purchase. Two of the nine salons are in Texas, and that is where the purchase stopped being only a retail decision.

## What's here

| Artifact | Format | What it is |
|---|---|---|
| [SkinRead DPIA](pdf/skinread_dpia.pdf) | [md](artifacts/skinread_dpia.md) | Draft v0.6: applicability analysis across Texas, Florida, and federal regimes; data inventory; necessity and proportionality; five findings with management responses; accepted and superseded risks; a costed remediation plan |

---

## Why a salon chain

Biometric capture has moved into ordinary retail. Smart mirrors, skin scanners, and AR try-on tools sit on salon floors, in cosmetics aisles, and in med-spas, sold as marketing equipment to buyers who have never negotiated a data clause. The kiosk in this scenario is well built. The exposure comes from the order form, a default consent screen nobody knew was editable, and a vendor retention setting that shipped turned off.

## The applicability work

Three of the determinations were close calls.

**HIPAA does not apply.** A skin and scalp report reads like health data, but Pineda is neither a covered entity nor a business associate. People get this wrong often in beauty-tech privacy discussions, so the assessment records the reasoning along with the conclusion.

**The Florida Digital Bill of Rights applies through one section.** Its controller obligations start at $1 billion in global revenue, which is why it is usually treated as a Big Tech statute. Its sensitive-data sale provision, § 501.715, reaches any for-profit business collecting personal data in Florida, so a small salon chain falls outside the first and inside the second.

**Texas CUBI drives the findings.** The 3D capture is a face-geometry record. CUBI requires notice and consent before capture, bars disclosure to third parties outside four narrow exceptions (none of which describes a processing vendor), requires destruction within a year of the purpose expiring, and carries a civil penalty of up to $25,000 per violation.

HB 149, the Texas Responsible AI Governance Act, changed that analysis in January 2026. Its new § 503.001(e)(2) exempts biometric processing involved in developing or offering AI systems unless the system uniquely identifies a person. SkinRead identifies no one, so the vendor's training use likely falls inside the exemption. Section 503.001(f) pulls those identifiers back under CUBI's destruction and penalty provisions if they are later used commercially outside it, and § 552.054(c) makes a CUBI violation a TRAIGA violation with its own penalty range and a mandatory 60-day cure period. These points are cited to the enrolled bill text; §10 of the DPIA lists which claims rest on statute and which on secondary sources.

## The finding worth reading

Four of the six stylists interviewed photograph clients' faces on personal phones, and two back those photos up to personal cloud accounts. The kiosk prompted the assessment, but the phones turned out to be the larger uncontrolled exposure, and they came to light by asking stylists what they do.

Pineda avoided issuing device rules because three locations use booth renters, and telling an independent contractor how to use her own phone raises worker-classification risk. That caution made sense at those three locations. It was then applied to the other six, where the stylists are W-2 employees and the concern does not exist, and the result was no policy anywhere. The recommendation splits accordingly: W-2 locations get a service-photo standard, booth-rental locations get a privacy clause at the next renewal, and the company privacy notice no longer claims to cover services Pineda does not control.

## The decision worth reading

Management disputed the consent-screen finding, argued the rating was overstated because only 37 Texas clients were affected, and declined to pause 3D capture while the screen was rewritten. v0.3 recorded that as an accepted risk (AR-2).

The assessor later declined to support it. Risk acceptance is a business judgment about exposure, and a likely statutory violation is not something the COO can accept alone. The resolution came from the vendor console: the original recommendation to suspend the kiosks was expensive, and management was right to resist it, but a 2D-only setting removes the biometric capture while leaving the retail recommendation flow running. It takes under an hour and costs nothing. AR-2 was superseded and the finding resolved on a setting. Two of the three most valuable remediations in the assessment are console settings that were available from the start.

## Skills demonstrated

- Multi-jurisdiction applicability analysis, including two determinations that are commonly gotten wrong
- Statutory verification against enrolled bill text, with secondary sources labeled
- Vendor risk analysis where the contract, rather than the architecture, is the failure point
- Condition, criteria, cause, effect, and evidence findings with management responses and one unresolved severity dispute
- Necessity and proportionality tied to measured business value ($38,412 in kiosk-attributed sales, with the 3D share untracked)
- Remediation planning with effort, cost, and owner, ordered so the free fixes land before the contract negotiation ends
- Recording encryption at rest as unable to test, because the vendor would not release its SOC 2 report without an NDA

## Scope and limitations

Stylist interviews covered six of 23 stylists, chosen by who was on shift during site visits, and the assessment calls this a convenience sample. Four questions remain open with counsel, including whether a 2D photo used only for skin analysis is a biometric identifier under CUBI, and whether providing images to a vendor for training is a sale of sensitive data under Texas or Florida law. The DPIA is a v0.6 draft pending counsel review.
