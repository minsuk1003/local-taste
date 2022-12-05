# SW_Capstone
## LOCAL TASTE - 현지인 기반 음식점 추천서비스

[프로젝트 소개]

현지인 기반 음식점 추천서비스 'LOCAL TASTE'입니다.
'현지인 맛집', '현지 입맛에 맞는 맛집'을 찾고 싶다면 해당 서비스를 이용하세요.

[프로젝트 개요]

저희가 보통 여행을 가서 맛집을 찾을 때 '현지인 맛집'을 찾고자 하는 경우가 종종 있습니다.
'현지인 맛집'을 찾게 되는 이유는 크게 2가지가 있습니다.

첫 번째로, 현지인들은 그 지역에 있는 많은 음식점을 알고 있을 것입니다. 따라서 현지인들은 해당 지역에서 제일 맛있는 음식점을 추천해줄 것이라고 기대할 수 있습니다.
만약 경희대생이 아닌 친구들이 경희대에 놀러오면, 우리도 이 지역의 현지인으로서 친구들에게 이 지역의 맛집을 알려줄 수 있습니다.

두 번째로, 현지 입맛에 맞는 음식점에 가고자 하는 외지인들이 있습니다. 대중적인 입맛과는 거리가 먼 음식점일지라도, 어떤 지역의 특색을 이해하기 위해 현지인들이 자주 가는 음식점을 찾아 방문하는 것입니다.

그러나, 현재 시중에는 현지인 맛집을 추천해주는 서비스는 없습니다. 따라서, 이번 작품에서 현지인 기반 음식점 추천서비스 - LOCAL TASTE를 구현하게 되었습니다.

[추천 방식]

'LOCAL TASTE'의 추천 방식은 구글 맵의 평점을 기반으로 합니다.
구글 맵의 리뷰 작성자를 현지인과 외지인으로 분류해서 현지인 평점과 외지인 평점을 구분합니다. 그리고 현지인 평점이 더 높은 음식점을 추천하게 됩니다.

이 때 신뢰할 수 있는 음식점만을 추천하기 위해, 20개 이상의 전체 리뷰 수, 5개 이상의 현지인 리뷰 수, 그리고 3.0 이상의 전체 평점을 기록한 음식점만을 추천합니다.

현지인 분류 기준은 5개 이상의 지역 내 리뷰 개수입니다. 현지인과 외지인을 분류하는데 있어 중요한 것은 사용자의 거주지보다도 해당 지역 내에 얼마나 많은 음식점을 방문했는지를 판단할 수 있는 정량적인 리뷰 개수이기 때문입니다.



시연 동영상 : https://www.youtube.com/watch?v=oXljLrR6cCA
