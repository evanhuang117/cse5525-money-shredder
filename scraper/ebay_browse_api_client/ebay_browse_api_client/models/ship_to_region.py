from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipToRegion")


@attr.s(auto_attribs=True)
class ShipToRegion:
    """This type is used provide details about included and excluded shipping regions.

    Attributes:
        region_id (Union[Unset, str]): The unique identifier of the shipping region. The value returned here is
            dependent on the corresponding <b>regionType</b> value. The <b>regionId</b> value for a region does not vary
            based on the eBay marketplace. However, the corresponding <b>regionName</b> value for a region is a localized,
            text-based description of the shipping region. <br><br> If the <b>regionType</b> value is
            <code>WORLDWIDE</code>, the <b>regionId</b> value will also be <code>WORLDWIDE</code>.<br><br> If the
            <b>regionType</b> value is <code>WORLD_REGION</code>, the <b>regionId</b> value will be one of the following:
            <code>AFRICA</code>, <code>AMERICAS</code>, <code>ASIA</code>, <code>AUSTRALIA</code>,
            <code>CENTRAL_AMERICA_AND_CARIBBEAN</code>, <code>EUROPE</code>, <code>EUROPEAN_UNION</code>,
            <code>GREATER_CHINA</code>, <code>MIDDLE_EAST</code>, <code>NORTH_AMERICA</code>, <code>OCEANIA</code>,
            <code>SOUTH_AMERICA</code>, <code>SOUTHEAST_ASIA</code> or <code>CHANNEL_ISLANDS</code>.<br><br>If the
            <b>regionType</b> value is <code>COUNTRY</code>, the <b>regionId</b> value will be the two-letter code for the
            country, as defined in the <a href="https://www.iso.org/iso-3166-country-codes.html " target="_blank">ISO
            3166</a> standard.<br><br>If the <b>regionType</b> value is <code>STATE_OR_PROVINCE</code>, the <b>regionId</b>
            value will either be the two-letter code for US states and DC (as defined on this <a
            href="https://www.ssa.gov/international/coc-docs/states.html " target="_blank">Social Security
            Administration</a> page), or the two-letter code for Canadian provinces (as defined by this <a
            href="https://www.canadapost.ca/tools/pg/manual/PGaddress-e.asp?ecid=murl10006450#1442131 "
            target="_blank">Canada Post</a> page).<br><br>If the <b>regionType</b> value is <code>COUNTRY_REGION</code>, the
            <b>regionId</b> value may be one of following: <code>_AH</code> (if a seller is not willing to ship to
            Alaska/Hawaii), <code>_PR</code> (if the seller is not willing to ship to US Protectorates), <code>_AP</code>
            (if seller is not willing to ship to a US Army or Fleet Post Office), and <code>PO_BOX</code> (if the seller is
            not willing to ship to a Post Office Box).
        region_name (Union[Unset, str]): A localized text string that indicates the name of the shipping region. The
            value returned here is dependent on the corresponding <b>regionType</b> value. <br><br> If the <b>regionType</b>
            value is <code>WORLDWIDE</code>, the <b>regionName</b> value will show <code>Worldwide</code>.<br><br> If the
            <b>regionType</b> value is <code>WORLD_REGION</code>, the <b>regionName</b> value will be a localized text
            string for one of the following large geographical regions: Africa, Americas, Asia, Australia, Central America
            and Caribbean, Europe, European Union, Greater China, Middle East, North America, Oceania, South America,
            Southeast Asia, or Channel Islands.<br><br>If the <b>regionType</b> value is <code>COUNTRY</code>, the
            <b>regionName</b> value will be a localized text string for any country in the world.<br><br>If the
            <b>regionType</b> value is <code>STATE_OR_PROVINCE</code>, the <b>regionName</b> value will be a localized text
            string for any US state or Canadian province. <br><br>If the <b>regionType</b> value is
            <code>COUNTRY_REGION</code>, the <b>regionName</b> value may be a localized version of one of the following:
            Alaska/Hawaii, US Protectorates, APO/FPO (Army or Fleet Post Office), or PO BOX.
        region_type (Union[Unset, str]): An enumeration value that indicates the level or type of shipping region.
            <br><br><b> Valid Values: </b> <ul><li><b> COUNTRY_REGION </b> - Indicates the region is a domestic region or
            special location within a country.</li><li><b> STATE_OR_PROVINCE </b> - Indicates the region is a state or
            province within a country, such as California or New York in the US, or Ontario or Alberta in
            Canada.</li><li><b> COUNTRY </b> - Indicates the region is a single country.</li><li><b> WORLD_REGION </b> -
            Indicates the region is a world region, such as Africa, the Middle East, or Southeast Asia.</li><li><b>
            WORLDWIDE </b> - Indicates the region is the entire world. This value is only applicable for included shiping
            regions, and not excluded shipping regions.</li></ul> For more detail on the actual
            <b>regionName</b>/<b>regionId</b> values that will be returned based on the <b>regionType</b> value, see the <a
            href="/api-
            docs/buy/browse/resources/item/methods/getItem#response.shipToLocations.regionExcluded.regionId">regionId</a>
            and/or <a href="/api-docs/buy/browse/resources/item/methods/getItem#response.shipToLocations.regionExcluded.regi
            onName">regionName</a> field descriptions.<br><br> Code so that your app gracefully handles any future changes
            to this list. For implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/ba:RegionTypeEnum'>eBay API documentation</a>
    """

    region_id: Union[Unset, str] = UNSET
    region_name: Union[Unset, str] = UNSET
    region_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_id = self.region_id
        region_name = self.region_name
        region_type = self.region_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if region_type is not UNSET:
            field_dict["regionType"] = region_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region_id = d.pop("regionId", UNSET)

        region_name = d.pop("regionName", UNSET)

        region_type = d.pop("regionType", UNSET)

        ship_to_region = cls(
            region_id=region_id,
            region_name=region_name,
            region_type=region_type,
        )

        ship_to_region.additional_properties = d
        return ship_to_region

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
