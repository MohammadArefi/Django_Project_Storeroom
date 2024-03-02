if ($('#map_todo_listing').length > 0) {
(function(A) {
	if (!Array.prototype.forEach)
		A.forEach = A.forEach || function(action, that) {
			for (var i = 0, l = this.length; i < l; i++)
				if (i in this)
					action.call(that, this[i], i, this);
			};

		})(Array.prototype);

		var
		mapObject,
		markers = [],
		markersData = {
			'Marker': [
			{
				name: 'رستوران ستاره آبی',
				location_latitude: 35.782570,
				location_longitude: 51.376428,
				map_image_url: 'assets/images/todo/map.jpg',
                map_marker: 'assets/images/icon/marker/5.png',
				todo_type: 'پیشنهاد ویژه',
				todo_type_class: 'services',
				rate: '4.8',
				rate_no: '19 رتبه بندی',
				url_point: 'listing-details.html',
                price: '<del>33000 تومان</del> - 12000 تومان',
                status: 'رزرو کنید',
                address: 'خیابان نیلوفر , کوچه مژده , ساختمان هستی',
				contact: '021 - 1234567'
			},
			{
				name: 'رستوران گنجی',
				location_latitude: 35.782161, 
				location_longitude: 51.380451,
				map_image_url: 'assets/images/todo/map.jpg',
				map_marker: 'assets/images/icon/marker/4.png',
				todo_type: 'هتل',
				todo_type_class: 'hotel',
				rate: '5',
				rate_no: '17 رتبه بندی',
				name_point: 'رستوران گنجی',
				url_point: 'listing-details-two.html',
				price: '<del>33000 تومان</del> - 12000 تومان',
                status: 'بسته',
                address: 'خیابان نیلوفر , کوچه مژده , ساختمان هستی',
                contact: '021 - 1234567'
			},
			{ 
				name: 'رستوران ستاره آبی',
				location_latitude: 35.777278,
				location_longitude: 51.373005,
				map_image_url: 'assets/images/todo/map.jpg',
				map_marker: 'assets/images/icon/marker/1.png',
				todo_type: 'کنسرت',
				todo_type_class: 'nightlife',
				rate: '3.5',
				rate_no: '17 رتبه بندی',
				name_point: 'رستوران ستاره آبی',
				url_point: 'listing-details.html',
				price: '<del>33000 تومان</del> - 12000 تومان',
                status: 'رزرو کنید',
                address: 'خیابان نیلوفر , کوچه مژده , ساختمان هستی',
                contact: '021 - 1234567'
			},
			{ 
				name: 'کافه دوستی',
				location_latitude: 35.780873,
				location_longitude: 51.369432,
				map_image_url: 'assets/images/todo/map.jpg',
				map_marker: 'assets/images/icon/marker/3.png',
				todo_type: 'رستوران',
				todo_type_class: 'restaurant',
				rate: '4.5',
				rate_no: '17 رتبه بندی',
				name_point: 'کافه دوستی',
				url_point: 'listing-details.html',
				price: '<del>33000 تومان</del> - 12000 تومان',
                status: 'رزرو کنید',
                address: 'خیابان نیلوفر , کوچه مژده , ساختمان هستی',
                contact: '021 - 1234567'
			},
			{
				name: 'چهار فصل توچال',
				location_latitude: 35.783606, 
				location_longitude: 51.372983,
				map_image_url: 'assets/images/todo/map.jpg',
				map_marker: 'assets/images/icon/marker/2.png',
				todo_type: 'خدمات',
				todo_type_class: 'services',
				rate: '5',
				rate_no: '17 رتبه بندی',
				name_point: 'چهار فصل توچال',
				url_point: 'listing-details.html',
				price: '<del>33000 تومان</del> - 12000 تومان',
                status: 'رزرو کنید',
                address: 'خیابان نیلوفر , کوچه مژده , ساختمان هستی',
                contact: '021 - 1234567'
			},
            {
				name: 'سالن زیبایی',
				location_latitude: 35.780338,
				location_longitude: 51.373391,
				map_image_url: 'assets/images/todo/map.jpg',
				map_marker: 'assets/images/icon/marker/1.png',
				todo_type: 'تخفیف',
				todo_type_class: 'services',
				rate: '4.5',
				rate_no: '17 رتبه بندی',
				name_point: 'بهشت اقیانوس',
				url_point: 'listing-details.html',
				price: '<del>33000 تومان</del> - 12000 تومان',
                status: 'رزرو کنید',
                address: 'خیابان نیلوفر , کوچه مژده , ساختمان هستی',
                contact: '021 - 1234567'
			}
			]

		};

			var mapOptions = {
				zoom: 16,
				center: new google.maps.LatLng(35.781052, 51.374507),
				mapTypeId: google.maps.MapTypeId.ROADMAP,

				mapTypeControl: false,
				mapTypeControlOptions: {
					style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
					position: google.maps.ControlPosition.LEFT_CENTER
				},
				panControl: false,
				panControlOptions: {
					position: google.maps.ControlPosition.TOP_RIGHT
				},
				zoomControl: true,
				zoomControlOptions: {
					position: google.maps.ControlPosition.RIGHT_BOTTOM
				},
				scrollwheel: false,
				scaleControl: false,
				scaleControlOptions: {
					position: google.maps.ControlPosition.TOP_LEFT
				},
				streetViewControl: true,
				streetViewControlOptions: {
					position: google.maps.ControlPosition.LEFT_TOP
				},
				styles: [
                    {
                    "featureType": "administrative",
                    "elementType": "labels.text.fill",
                    "stylers": [
                    {
                    "color": "#444444"
                    }
                    ]
                    },
                    {
                    "featureType": "landscape",
                    "elementType": "all",
                    "stylers": [
                    {
                    "color": "#f2f2f2"
                    }
                    ]
                    },
                    {
                    "featureType": "poi",
                    "elementType": "all",
                    "stylers": [
                    {
                    "visibility": "off"
                    }
                    ]
                    },
                    {
                    "featureType": "road",
                    "elementType": "all",
                    "stylers": [
                    {
                    "saturation": -100
                    },
                    {
                    "lightness": 45
                    }
                    ]
                    },
                    {
                    "featureType": "road.highway",
                    "elementType": "all",
                    "stylers": [
                    {
                    "visibility": "simplified"
                    }
                    ]
                    },
                    {
                    "featureType": "road.arterial",
                    "elementType": "labels.icon",
                    "stylers": [
                    {
                    "visibility": "off"
                    }
                    ]
                    },
                    {
                    "featureType": "transit",
                    "elementType": "all",
                    "stylers": [
                    {
                    "visibility": "off"
                    }
                    ]
                    },
                    {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": [
                    {
                    "color": "#cfcfcf"
                    },
                    {
                    "visibility": "on"
                    }
                    ]}],
			};
			var marker;
			mapObject = new google.maps.Map(document.getElementById('map_todo_listing'), mapOptions);
			for (var key in markersData)
				markersData[key].forEach(function (item) {
                    marker = new google.maps.Marker({
						position: new google.maps.LatLng(item.location_latitude, item.location_longitude),
						map: mapObject,
						icon: item.map_marker,
					});
					if ('undefined' === typeof markers[key])
						markers[key] = [];
					markers[key].push(marker);
					google.maps.event.addListener(marker, 'click', (function () {
				  closeInfoBox();
				  getInfoBox(item).open(mapObject, this);
				  mapObject.setCenter(new google.maps.LatLng(item.location_latitude, item.location_longitude));
				 }));

	});

	new MarkerClusterer(mapObject, markers[key]);
	
		function hideAllMarkers () {
			for (var key in markers)
				markers[key].forEach(function (marker) {
					marker.setMap(null);
				});
		};
	
	

		function closeInfoBox() {
			$('div.infoBox').remove();
		};

		function getInfoBox(item) {
			return new InfoBox({
				content:
					'<div class="marker_info" id="marker_info"> <div class="todo-item">' + 
						'<div class="todo-thumbnail-area">' +
							'<div class="item-thumb"><img src="' + item.map_image_url + '" alt=""/></div>' +
							'<div class="todo-overlay-info">' + 
								'<div class="todo-type-cat"><a href="#" class="' + item.todo_type_class + '">' + item.todo_type + '</a>' + '</div>'+
								'<div class="todo-meta-bottom">' + 
									'<div class="todo-rating"><span>'+ item.rate +'</span>' + item.rate_no + '</div>'+
									'<div class="save"><a href="#"><i class="fa fa-heart"></i></a>' + '</div>'+
								'</div>' + 
							'</div>' + 
						'</div>' + 
						'<div class="todo-content">' +
							'<h3 class="title"><a href="'+item.url_point+'">'+ item.name +'</a></h3>' +
							'<div class="todo-price-status">'+
								'<div class="todo-price">'+ item.price +'</div>' +
								'<div class="todo-status">'+ item.status +'</div>' +
							'</div>' +
							'<div class="todo-meta">'+
								'<div class="todo-location"><span class="icon-location"></span>'+ item.address +'</div>' +
								'<div class="todo-number"><span class="icon-phone"></span>'+ item.contact +'</div>' +
							'</div>' +
						'</div>' +
					'</div>',
				disableAutoPan: false,
				maxWidth: 0,
				pixelOffset: new google.maps.Size(10, 92),
				closeBoxMargin: '',
				isHidden: false,
				alignBottom: true,
				pane: 'floatPane',
				enableEventPropagation: true
			});
		};
function onHtmlClick(location_type, key){
     google.maps.event.trigger(markers[location_type][key], "click");
}
}