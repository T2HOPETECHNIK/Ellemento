import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class Tray extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  tray_id?: number;
  
  @property({
    type: 'string',
    required: true,
  })
  tray_name: string;

  @property({
    type: 'number',
    required: true,
  })
  location_id: number;

  @property({
    type: 'number',
    required: true,
  })
  stage_id: number;

  @property({
    type: 'date',
    required: true,
  })
  date_time_start: string;

  @property({
    type: 'date',
    required: true,
  })
  date_time_end: string;

  @property({
    type: 'number',
  })
  locationId?: number;
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<Tray>) {
    super(data);
  }
}

export interface TrayRelations {
  // describe navigational properties here
}

export type TrayWithRelations = Tray & TrayRelations;
